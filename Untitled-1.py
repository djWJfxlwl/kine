import discord
token = "OTAwNzI5ODkwNTYxNzM2NzA1.YXFkFA.F-N_nZoowRO9JU9yz6aTUBSRes0"
client = discord.Client()
@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message):
    if message.content == '레칸아 키네':
        await message.channel.send('죽빡미만')
    if message.content == '레칸아 죽으니까빡치지?':
        await message.channel.send('창조주')
    if message.content == '레칸아 아비게일':
        await message.channel.send('슽리1등!')
    if message.content == '레칸아':
        await message.channel.send('네?')
    if message.content == '레칸아 뭐해?':
        await message.channel.send('놀고있었어요')
    if message.content == '레칸아 지라치':
        await message.channel.send('사회주의 최1고의 지랒이')
    if message.content == '레칸아 안녕':
        await message.channel.send('안녕하세요!')
    if message.content =='레칸아 굿모닝':
        await message.channel.send('굿모닝! 좋은 아침이네요')
    if message.content == '레칸아 굿나잇':
        await message.channel.send('굿나잇!잘자요')

client.run(token)
