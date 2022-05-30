import allure
import pytest

from page_objets.ProductCard import ProductCard


@allure.title("Добавление нового товара в разделе администратора.")
@pytest.mark.skip(reason="use only with local opencard")
def test_add_new_item(browser, admin_page):
    admin_page.choose_product_catalog()
    admin_page.create_new_product()
    product_page = ProductCard(browser)
    product_page.fill_product_name()
    product_page.fill_model_name()
    product_page.save_product()
    assert admin_page.check_alert_text == "Success: You have modified products!"


@allure.title("Удаление товара из списка в разделе администратора")
@pytest.mark.skip(reason="use only with local opencard")
def test_remove_product(browser, admin_page):
    admin_page.choose_product_catalog()
    admin_page.find_created_product()
    admin_page.delete_created_product()
    admin_page.accept_alert()
    assert admin_page.check_alert_text == "Success: You have modified products!"

    product_page = ProductCard(browser)
    assert product_page.check_empty_product_list() == "No results!"
    