from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

        # list_display = [field.name for field in Subscriber._meta.fields]  # вывод всех полей
        # # exclude = ['email'] # исключает показ поля на странице
        # # fields = ['email'] # показывать только эти поля на странице
        # list_filter = ['name', ]  # фильтр по столбцу
        # search_fields = ['name', 'email']  # поиск по столбцам

    def get_absolute_url(self):  # Конвенция для получения URL-адреса данного объекта
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Partner(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.CharField(max_length=200, db_index=True, unique=True)
    # Иконка партнёра.
    image = models.ImageField(upload_to='products/partner/%s' % name, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'

    def __str__(self):
        return self.name


# blank = True если вы хотите разрешить пустые значения в формах
# null = True При True Django сохранит пустое значение как NULL в базе данных. Значение по умолчанию – False
# default =Значение по умолчанию для поля.
class Product(models.Model):
    # Это ForeignKey модели Category.Это отношение "многие к одному": продукт относится к одной категории, а
    # категория содержит несколько продуктов
    # CASCADE - при удалении или изменении записи в первичной таблице, также удалить связанные записи вторичной таблицы

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Категория")
    # Партнёр
    partner = models.ForeignKey(Partner, related_name='partner', on_delete=models.CASCADE, verbose_name="Партнёр")
    # Название продукта.
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название товара")
    # Алиас продукта(его URL).
    slug = models.SlugField(max_length=200, db_index=True)
    # Изображение продукта.
    image = models.ImageField(upload_to='products/', blank=True)
    # Необязательное описание для продукта.
    description = models.TextField(blank=True, verbose_name="Описание")
    # Это поле DecimalField.В нем используется десятичное число Python.Десятичный тип для хранения десятичного
    # числа с фиксированной точностью.Максимальное число цифр(включая десятичные разряды) задается с
    # помощью атрибута max_digits и десятичных знаков с атрибутом decimal_places
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    # Это поле PositiveIntegerField для хранения остатков данного продукта
    stock = models.PositiveIntegerField(verbose_name="Доступный остаток")
    # Это булево значение, указывающее, доступен  ли продукт  или  нет.Позволяет включить / отключить
    # продукт в каталоге.
    available = models.BooleanField(default=True, verbose_name="Статус товара")
    # Это поле хранит дату когда был создан объект.
    # auto_now = True Значение поля будет автоматически установлено в текущую дату при каждом сохранении объекта
    # auto_now_add Значение поля будет автоматически установлено в текущую дату при создании(первом сохранении) объекта
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    # В этом поле хранится время последнего обновления объекта
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")

    class Meta:
        ordering = ('name',)  # сортировка
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Конвенция для получения URL-адреса данного объекта
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
