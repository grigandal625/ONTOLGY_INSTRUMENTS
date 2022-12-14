from django.db import models
from django.utils.translation import gettext_lazy as _
from ontology_model.models import ReflexivityChoices, SymmetryChoices, TransitivityChoices, ElementType, RelationType

# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    extension = models.CharField(max_length=255, verbose_name="Расширение")
    content = models.FileField(verbose_name='Содержимое')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return f'{self.name}.{self.extension}'


class Element(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")
    type = models.ForeignKey(
        ElementType, on_delete=models.RESTRICT, verbose_name="Тип элемента")
    data = models.JSONField(null=True, blank=True,
                            verbose_name="Содержимое")
    files = models.ManyToManyField(File, verbose_name="Файлы", blank=True)

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return f'{self.name} ({self.type})'


class CustomReflexivityChoices(models.IntegerChoices):
    default = 0, _('По умолчанию')
    reflexive = ReflexivityChoices.reflexive
    antireflexive = ReflexivityChoices.antireflexive
    __empty__ = ReflexivityChoices.__empty__


class CustomSymmetryChoices(models.IntegerChoices):
    default = 0, _('По умолчанию')
    symmetric = SymmetryChoices.symmetric
    antisymmetric = SymmetryChoices.antisymmetric
    __empty__ = SymmetryChoices.__empty__


class CustomTransitivityChoices(models.IntegerChoices):
    default = 0, _('По умолчанию')
    transitive = TransitivityChoices.transitive
    intransitive = TransitivityChoices.intransitive


class Relation(models.Model):
    parent = models.ForeignKey(
        Element, on_delete=models.CASCADE, verbose_name="Родительский элемент", related_name="output")
    child = models.ForeignKey(
        Element, on_delete=models.CASCADE, verbose_name="Дочерний элемент", related_name="input")
    type = models.ForeignKey(
        RelationType, on_delete=models.RESTRICT, verbose_name="Тип связи")
    name = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name="Имя")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")
    data = models.JSONField(null=True, blank=True,
                            verbose_name="Содержимое")
    reflexivity = models.IntegerField(
        null=True, blank=True, default=CustomReflexivityChoices.default,
        choices=CustomReflexivityChoices.choices, verbose_name="Антирефлексивность")
    symmetry = models.IntegerField(
        null=True, blank=True, default=CustomSymmetryChoices.default,
        choices=CustomSymmetryChoices.choices, verbose_name="Симметричность")
    transitivity = models.IntegerField(
        default=CustomTransitivityChoices.default, choices=CustomTransitivityChoices.choices, verbose_name="Транзитивность")

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'

    def __str__(self):
        if self.name:
            return f'{self.name} - {self.type}'
        return str(self.type)
