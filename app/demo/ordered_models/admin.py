from django.contrib import admin

from ordered_model.admin import (
    OrderedModelAdmin,
    OrderedTabularInline,
    OrderedInlineModelAdminMixin,
    OrderedStackedInline)

from .models import Item, PizzaToppingsThroughModel, Pizza, Topping, Answer, Question, TestUser


class ItemAdmin(OrderedModelAdmin):
    verbose_name = "dsadsa"
    verbose_name_plural = "dsadsas"
    list_display = ("name", "move_up_down_links")


class PizzaToppingTabularInline(OrderedTabularInline):
    model = PizzaToppingsThroughModel
    fields = ("topping", "quantity", "order", "move_up_down_links",)
    readonly_fields = ("order", "move_up_down_links")
    ordering = ("order",)
    autocomplete_fields = ("topping",)

class PizzaToppingStackedInline(OrderedStackedInline):
    model = PizzaToppingsThroughModel
    fields = ("topping", "quantity", "order", "move_up_down_links",)
    readonly_fields = ("order", "move_up_down_links")
    ordering = ("order",)
    autocomplete_fields = ("topping",)

class PizzaAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Pizza
    list_display = ("name",)
    inlines = (PizzaToppingTabularInline,)


class AnswerTabularInline(OrderedTabularInline):
    model = Answer
    fields = ("text", "user", "order", "move_up_down_links",)
    readonly_fields = ("order", "move_up_down_links")


class AnswerStackedInline(OrderedStackedInline):
    model = Answer
    fields = ("text", "user", "order", "move_up_down_links",)
    readonly_fields = ("order", "move_up_down_links")
    # raw_id_fields = ("user",)

class QuestionAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    fields = ("text",)
    inlines = [
        # AnswerTabularInline,
        AnswerStackedInline
    ]


class ToppingAdmin(admin.ModelAdmin):
    search_fields = ("name",)

admin.site.register(Item, ItemAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(TestUser)
admin.site.register(Question, QuestionAdmin)
