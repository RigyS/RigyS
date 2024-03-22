import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak discorda giriş yaptık!')

@bot.command()
async def yardım(ctx):
    with open("yardım.txt", "r", encoding="utf-8") as yardım:
        metin = yardım.read()
    await ctx.send(file = metin)

@bot.command()
async def Çevre_Kirliliği_Nedir(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Bu Botu Kullanarak Doğamızı Koruyorsun; Çevre kirliliği, doğal çevreye atılan zararlı maddelerin, enerjinin veya diğer unsurların, insan sağlığına, ekosistemlere ve çevre kalitesine zarar veren durumu ifade eder. Bu zararlı maddeler hava, su, toprak veya gürültü gibi çevresel unsurları etkileyebilir. Çevre kirliliği genellikle sanayi, tarım, enerji üretimi, taşımacılık ve atık yönetimi gibi insan etkinliklerinden kaynaklanır.")

@bot.command()
async def Çevre_Kirliliğini_Nasıl_Önleriz(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Bu Botu Kullanarak Doğamızı Koruyorsun; Geri dönüşüm ve atık yönetimi: Atıkların geri dönüşümü ve doğru şekilde yönetilmesi. Temiz enerji kullanımı: Fosil yakıtların yerine yenilenebilir enerji kaynaklarının tercih edilmesi. Çevre dostu taşımacılık: Toplu taşıma, bisiklet kullanımı gibi çevre dostu alternatiflerin benimsenmesi. Endüstriyel ve ticari faaliyetlerde çevresel standartlara uyum: Temiz teknolojilerin kullanımı ve atık yönetimi uygulamalarının iyileştirilmesi. Bilinçli tüketim alışkanlıkları: Az ambalajlı ürünlerin tercih edilmesi ve tek kullanımlık ürünlerden kaçınılması. Eğitim ve farkındalık: Çevre konusunda toplumu eğitmek ve bilinçlendirmek için faaliyetler düzenlenmesi.")

@bot.command()
async def Çevre_Kirliliği_Hakkında_Görsel(ctx):
    resimler_listesi = os.listdir('images')
    resim = random.choice(resimler_listesi)
    with open(f'images{resim}', 'rb') as f:
        resim1 = discord.File(f)
    await ctx.send(file=resim1)

bot.run("")