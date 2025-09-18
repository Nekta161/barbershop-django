---
st_group: python 413
project: "[[Академия TOP]]"
journal: "[[PYTHON413]]"
tags:
  - PYTHON413
  - django
  - cbv
  - class-based-views
  - refactoring
  - ListView
  - DetailView
  - CreateView
  - TemplateView
date: 2025-08-02
type:
  - home work
hw_num: 46
topic: Рефакторинг проекта на классовые представления (CBV)
hw_theme:
  - django
  - Class-Based Views
  - refactoring
---

# Домашнее задание 📃

**Рефакторинг проекта "Барбершоп" на классовые представления (CBV)**

## Краткое содержание

>[!info]
>
>### Краткое содержание
>
>В этом задании вы выполните важный шаг в профессиональном развитии Django-разработчика — проведете рефакторинг существующего кода. Ваша задача — переписать все функциональные представления (FBV) в приложении `core` на их классовые аналоги (CBV). Это позволит сделать код более структурированным, читаемым и расширяемым, а также лучше понять принципы ООП в контексте Django.

### Технологии: 🦾

- Python 3.10+
- Django 4.x+
- Django Class-Based Views (CBV):
  - `TemplateView`
  - `ListView`
  - `DetailView`
  - `CreateView`
- Django ORM

## Задание 👷‍♂️

Вам предстоит провести рефакторинг всех представлений в приложении `core`. Каждое функциональное представление должно быть заменено соответствующим классом.

### Часть 1: Простые представления (`TemplateView`)

1. **Главная страница (`landing`):**
    - Создайте класс `LandingView`, унаследованный от `django.views.generic.TemplateView`.
    - Укажите `template_name = 'landing.html'`.
    - Для передачи в шаблон списков мастеров и отзывов переопределите метод `get_context_data`. Внутри него получите данные из БД и добавьте их в контекст.

2. **Страница благодарности (`thanks`):**
    - Создайте класс `ThanksView`, унаследованный от `TemplateView`.
    - Укажите `template_name = 'thanks.html'`.

### Часть 2: Представления для отображения списков и деталей (`ListView`, `DetailView`)

1. **Список заявок (`orders_list`):**
    - Создайте класс `OrdersListView`, унаследованный от `django.views.generic.ListView`.
    - Укажите `model = Order`, `template_name = 'orders_list.html'`, `context_object_name = 'orders'`.
    - Для сортировки по убыванию даты создания переопределите `queryset` или укажите атрибут `ordering = ['-date_created']`.
    - **Перенесите логику поиска:** логику фильтрации по Q-объектам из функционального представления перенесите в метод `get_queryset`. В этом методе сначала получайте базовый `queryset`, а затем применяйте к нему фильтры на основе GET-параметров из `self.request.GET`.

2. **Детальная информация о заявке (`order_detail`):**
    - Создайте класс `OrderDetailView`, унаследованный от `django.views.generic.DetailView`.
    - Укажите `model = Order`, `template_name = 'order_detail.html'`, `context_object_name = 'order'`.

### Часть 3: Представления для создания объектов (`CreateView`)

1. **Создание отзыва (`create_review`):**
    - Создайте класс `ReviewCreateView`, унаследованный от `django.views.generic.CreateView`.
    - Укажите `model = Review`, `form_class = ReviewForm`, `template_name = 'review_form.html'`.
    - Для редиректа после успешного создания отзыва используйте `success_url = reverse_lazy('thanks')`.
    - **Для добавления success-сообщения** переопределите метод `form_valid`. Внутри него вызовите `messages.success()` перед вызовом родительского метода.

2. **Создание заявки (`create_order`):**
    - Создайте класс `OrderCreateView`, унаследованный от `CreateView`.
    - Укажите `model = Order`, `form_class = OrderForm`, `template_name = 'order_form.html'`, `success_url = reverse_lazy('thanks')`.
    - Аналогично `ReviewCreateView`, переопределите `form_valid` для добавления flash-сообщения об успехе.

>[!warning]
>
>### Важные моменты
>
>- Не забудьте обновить файл `core/urls.py`, чтобы он использовал новые классовые представления. Вместо `views.my_view` теперь будет `views.MyView.as_view()`.
>- Внимательно перенесите всю логику из старых представлений в методы новых классов. Особенно это касается логики поиска и добавления данных в контекст.

### Часть 4: Обновление `urls.py`

- Откройте файл `core/urls.py`.
- Замените все вызовы функциональных представлений на вызовы методов `.as_view()` от ваших новых классов.

Пример:
`path('orders/', views.orders_list, name='orders_list')`
превратится в
`path('orders/', views.OrdersListView.as_view(), name='orders_list')`

### Таблица рефакторинга

| Функциональное представление (FBV) | Классовое представление (CBV) | Базовый класс Django |
| :--- | :--- | :--- |
| `landing` | `LandingView` | `TemplateView` |
| `thanks` | `ThanksView` | `TemplateView` |
| `orders_list` | `OrdersListView` | `ListView` |
| `order_detail` | `OrderDetailView` | `DetailView` |
| `create_review` | `ReviewCreateView` | `CreateView` |
| `create_order` | `OrderCreateView` | `CreateView` |

## Критерии проверки 👌

1. **Рефакторинг на `TemplateView` и `DetailView` (3 балла)**
    - Представления `landing`, `thanks` и `order_detail` переписаны на CBV.
    - `LandingView` корректно передает дополнительный контекст (мастера, отзывы) через `get_context_data`.
    - `OrderDetailView` корректно настроен для отображения одного объекта.

2. **Рефакторинг `ListView` с поиском (5 баллов)**
    - Представление `orders_list` переписано на `ListView`.
    - Логика поиска по Q-объектам корректно перенесена в метод `get_queryset`.
    - Сортировка по дате создания работает корректно.

3. **Рефакторинг `CreateView` с обработкой формы (3 балла)**
    - Представления `create_review` и `create_order` переписаны на `CreateView`.
    - Корректно указаны `form_class`, `template_name` и `success_url`.
    - Flash-сообщения об успехе добавляются через переопределение метода `form_valid`.

4. **URL-конфигурация и общее качество (1 балл)**
    - Файл `core/urls.py` обновлен и использует `.as_view()` для всех маршрутов.
    - Код соответствует PEP 8, структура классов логична и чиста.
    - Проект работает без ошибок после рефакторинга.
