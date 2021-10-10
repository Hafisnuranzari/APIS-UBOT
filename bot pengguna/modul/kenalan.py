from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.r(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai Perkenalkan Namaku Hapis`")
    sleep(3)
    await typew.edit("Umur Tak Terbatas`")
    sleep(1)
    await typew.edit("`Tinggal Di dalem rumah lah tolo, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Banget Sama`")
    sleep(1)
    await typew.edit("`Tapi Boong,Tapi Beneran Kok Sayang 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Nyerah`")
    sleep(1)
    await typew.edit("`Dan Selalu Insecure`")
# Create by myself @localheart
