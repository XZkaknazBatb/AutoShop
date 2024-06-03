from django.shortcuts import get_object_or_404, render
from goods.models import Categories, Products


def catalog(request, category_slug=False):

    bmvd = False
    category = False
    parent_categories = False
    categories = False
    goods = Products.objects.none()

    if category_slug:

        category = get_object_or_404(Categories, slug=category_slug)

        if category_slug == "dvigatel":
            parent_categories = category.get_ancestors(include_self=True)
            categories = category.get_children()
            goods = Products.objects.filter(category__in=categories)

        elif category_slug in get_object_or_404(
            Categories, slug="dvigatel"
        ).get_children().values_list("slug", flat=True):
            parent_categories = category.get_ancestors(include_self=True)
            categories = get_object_or_404(
                Categories, slug="dvigatel"
            ).get_children()
            goods = Products.objects.filter(category__slug=category_slug)

        elif category_slug == "bmvd":
            bmvd = True
            goods = Products.objects.filter(category__slug=category_slug)

        else:
            parent_categories = category.get_ancestors(include_self=True)
            bmvd_category = get_object_or_404(Categories, slug='bmvd')
            categories = Categories.objects.exclude(id=bmvd_category.id)
            goods = Products.objects.filter(category__slug=category_slug)

        title = f"Каталог {category.name} | АвтоМир"

    else:
        bmvd_category = get_object_or_404(Categories, slug='bmvd')
        categories = Categories.objects.exclude(id=bmvd_category.id)
        goods = Products.objects.exclude(category=bmvd_category)
        title = "Каталог Двигатели | АвтоМир"

    context = {
        "title": title,
        "bmvd": bmvd,
        "category": category,
        "parent_categories": parent_categories,
        "categories": categories,
        "goods": goods,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    if product.category.slug == "bmvd":
        bmvd_product = True
    else:
        bmvd_product = False

    if bmvd_product:
        title = f"БМВД {product.name} | АвтоМир"
    else:
        title = f"Двигатели {product.name} | АвтоМир"

    if product.advantages:
        advantages_list = product.advantages.split("\n")
    else:
        advantages_list = None

    

    context = {
        "title": title,
        "product": product,
        "bmvd_product": bmvd_product,
        "advantages_list": advantages_list
    }

    return render(request, "goods/product.html", context)
