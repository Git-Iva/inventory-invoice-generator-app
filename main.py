import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype="str")

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.article_name = df.loc[df["id"] == article_id, "name"].squeeze()
        self.article_price = df.loc[df["id"] == article_id, "price"].squeeze()

    def available(self):
        """checks if article is available """
        availability = df.loc[df["id"] == self.article_id, "in stock"].squeeze()
        return int(availability)

    #def buy(self):
       # """ reduce the number of stock when an item is bought"""
       # df.loc[df["id"] == self.article_id, "in stock"] -= 1
       # new_stock = self.stock - 1
       #df.to_csv("articles.csv", index=False)
       #return new_stock

class Invoice:
    def __init__(self,):
        self.invoice_number = df.loc
        [df["id"] == article.article_id, "id"].squeeze()

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice nr: {self.invoice_number}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {article.article_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {article.article_price}", ln=1)

        pdf.output("receipt.pdf")


article_id = input("Enter the id of the product you want to buy:")
article = Article(article_id=article_id)
if article.available():
    invoice = Invoice()
    invoice.generate()
else:
    print("Article not in stock")
