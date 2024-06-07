
import discord
import requests
from discord.ext import commands



@bot.command(name='clear')
async def delete_messages(ctx):
    channel_id = ctx.channel.id
    channel = bot.get_channel(channel_id)

    if not channel:
        await ctx.send("รหัสช่องไม่ถูกต้อง โปรดระบุรหัสช่องที่ถูกต้อง")
        return

    try:
        await ctx.send(f"การลบข้อความ การดำเนินการนี้อาจใช้เวลาสักครู่... {ctx.author.mention}")

        messages = []
        async for message in channel.history(limit=None):
            messages.append(message)

        chunk_size = 100 
        for i in range(0, len(messages), chunk_size):
            await channel.delete_messages(messages[i:i + chunk_size])

        await ctx.send(f"ข้อความทั้งหมดที่ถูกลบในช่อง {ctx.author.mention}")
    except discord.Forbidden:
        await ctx.send("Game Security ไม่มีสิทธิ์ที่จำเป็นในการลบข้อความในช่องนั้น")


        bot.run("herer")
