import discord
import os
import praw
import random
from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
players = {}
reddit = praw.Reddit(
  client_id = os.environ['client_id'],
  client_secret = os.environ['client_secret'],
  username = os.environ['username'],
  password = os.environ['password'],
  user_agent = "<ReplyCommentBot1.0>",
  check_for_async=False
)

client = commands.Bot(command_prefix = "$")

def get_quote():
  begin = "не, ок, да ок, стига, не стига, ай стига, чил, ок чил, тру, уат, е, еда".split(', ')
  mid = "акчуъли, кайнда, лоукий, наистина, буквално".split(', ')
  end = "страшното великото тъжното странния лошия злия тролиш ретарда трола лъкера ънлъкерите лъкерите ънлъкера източника ограничения комплексаря фейка".split()
  final = "лол, лмао, наистина, не знам".split(', ')
  solo = "така е, наистина, :neutral_face:, не е фън, ехелие, о цуне, великото ли е, даедае, така е, не си забавен, gg, слаб си, няя нужда, кутиран като рибка, окото, трол гаден, тва ти ли си, криндж, ratio, didnt ask, даедае, тихо ве, не млъкни, млъкни ве, бягайве, АЙ СТИГА ай стига не наистина стига, brixton bullies, cap, кап, черните имали права :billed_cap:, денисът, marto operator merchant gaden, typi gadni cherni izrodi, мане козата, меси е слабак, гномеси 10, - Защо негрите миришат? - За да може и слепите да ги мразят!, - Кога ще изчезне расизмът? - Когато расистите станат далтонисти., Въпрос: Какво разделя хората от маймуните? Отговор: Средиземно море., Въпрос: Защо на негрите са им широки ноздрите? Отговор: Защото са им дебели пръстите!, Каква е разликата между пицата и евреина? - Пицата не крещи като я сложиш в пещта., - Искам шоколад! Искам шоколад! - крещи малко канибалче. Бащата е нервен. - Млъкни!! Откъде да ти намеря негър в три часа през нощта?!, - Каква е мечтата на средния американец? - Негрите да си отидат в Африка и под всяка мишница да носят по един евреин., Как бяга евреин от концлагер? Ами скача в пещта и дим да го няма!, След цял ден тежък труд двама евреи си говорят на връщане към концлагера: - Май ще ядем карамел! - усмихва се единият. - Надявай се. Горят диабетиците. - казал приятелят му., :flushed:, козалдо, песи, sage heal me, ок въглен, стига си спамил ве, утре петкова страшното, хуу ай, *dies from cringe*, уат тва как не го хитва, месру трол гаден, не аз повече няя играя с вас, за забавен ли се мислиш, дени слабак, стига си тролил, денисът слаква киловете, чупапи, харесвам jett, walking L, https://www.twitch.tv/mamabenjyfishy1, https://youtu.be/svxwIa5mxjQ, https://youtu.be/2xWkATdMQms, бабата на иван е окото, ок димак, здравейте във ново видео на канала ми momo05, цуне е източника, момо е източника, иван е източника, ракът, ЍЍЍЍЍЍЍЍЍЍЍ".split(', ')
  i = random.randint(0,989)
  if i < 910:
    i = random.randint(0,11)
    if i == 0:
        return(solo[random.randint(0,len(solo)-1)])
    elif i == 1:
        return(final[random.randint(0,len(final)-1)])
    elif i == 2:
        return(end[random.randint(0,len(end)-1)])
    elif i == 3:
        return(end[random.randint(0,len(end)-1)]+' '+final[random.randint(0,len(final)-1)])
    elif i == 4:
        return(mid[random.randint(0,len(mid)-1)]+' '+end[random.randint(0,len(end)-1)])
    elif i == 5:
        return(mid[random.randint(0,len(mid)-1)]+' '+end[random.randint(0,len(end)-1)]+' '+final[random.randint(0,len(final)-1)])
    elif i == 6:
        return(begin[random.randint(0,len(begin)-1)])
    elif i == 7:
        return(begin[random.randint(0,len(begin)-1)]+' '+end[random.randint(0,len(end)-1)])
    elif i == 8:
        return(begin[random.randint(0,len(begin)-1)]+' '+end[random.randint(0,len(end)-1)]+' '+final[random.randint(0,len(final)-1)])
    elif i == 9:
        return(begin[random.randint(0,len(begin)-1)]+' '+final[random.randint(0,len(final)-1)])
    elif i == 10:
        return(begin[random.randint(0,len(begin)-1)]+' '+mid[random.randint(0,len(mid)-1)]+' '+end[random.randint(0,len(end)-1)])
    elif i == 11:
        return(begin[random.randint(0,len(begin)-1)]+' '+mid[random.randint(0,len(mid)-1)]+' '+end[random.randint(0,len(end)-1)]+' '+final[random.randint(0,len(final)-1)])
  elif i < 990:
    return(solo[random.randint(0,len(solo)-1)])

def get_prediction():
  prediction = 'да, не, не знам'.split(', ')
  return(prediction[random.randint(0,len(prediction)-1)])

def get_ship():
  return('тази връзка я оценявам в '+str(random.randint(0,100))+'%')


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="Fortnite"))


@client.command()
async def post(ctx, subred = "cursedimages"):
  subreddit = reddit.subreddit(subred)
  all_subs = []
  hot = subreddit.hot(limit=100)

  for submission in hot:
    all_subs.append(submission)
  
  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url
  text = random_sub.selftext

  em = discord.Embed(title = name, description = text)
  em.set_image(url = url)
  await ctx.send(embed = em)

@client.command()
async def repeat(ctx, *, arg: str):
    await ctx.send(arg)

@client.command()
async def quote(ctx):
  i = random.randint(0,1000)
  if i < 980:
    quote = get_quote()
    await ctx.send(quote)
  else:
    dir = "momo"
    await ctx.send(file=discord.File('momo/'+random.choice(os.listdir(dir))))

@client.command()
async def guess(ctx):
  await ctx.send(get_prediction())

@client.command()
async def ship(ctx):
  await ctx.send(get_ship())

@client.command()
async def rand(ctx):
  subreddit = reddit.subreddit("all")
  all_subs = []
  new = subreddit.new(limit=100)

  for submission in new:
    all_subs.append(submission)
  
  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url
  text = random_sub.selftext

  em = discord.Embed(title = name, description = text)
  em.set_image(url = url)

  await ctx.send(embed = em)
  
client.load_extension("musicbot")

keep_alive()
client.run(os.environ['token'])
