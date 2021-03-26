
class EndPoint:
    BASE_URI_API = "https://bookstore.toolsqa.com/BookStore/v1/Books"
    BASE_URI_UI = "https://www.flipkart.com/"
    ProductSearch = "samsung galaxy m31 6gb 64gb"

class Flipkart:
    LoginPopupCancel = "//button[contains(text(),'✕')]"
    SearchTextBox = "//div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]"
    SearchButton = "//div[2]/div[2]/form[1]/div[1]/button[1]/*[1]"
    ProductLink = "//div[contains(text(),'SAMSUNG Galaxy M31 (Ocean Blue, 64 GB)')]"
    ProductPrice = "//div[3]/div[1]/div[4]/div[1]/div[1]/div[1]"
    AddToCartButton = "//div[1]/div[2]/div[1]/ul[1]/li[1]/button[1]"
    CartAddQuantity = "//button[@class='_23FHuj'][2]"
    CartTotalPrice = "//div[1]/span[1]/div[1]/div[1]/span[1]"


class Amazon:
    SearchTextBox = "//input[@id='twotabsearchtextbox']"
    SearchButton = "//input[@id='nav-search-submit-button']"
    ProductLink = "//span[contains(text(),'Samsung Galaxy M31 6GB 64GB (Ocean Blue)')]"
    ProductPrice = "//span[@id='priceblock_ourprice']"
    AddToCartButton = "//input[@id='add-to-cart-button']"
    CartTotalPrice = "//div[1]/div[1]/div[1]/div[1]/span[1]/span[2]"

