from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.ghosting(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu jelek`")
    sleep(2)
    await typew.edit("`Kedua kamu ya kamu jelek`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu memang jelek jadi di ghosting tolol`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi,Ku pantau Kau Anjing..**")


@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Vicky Peler☑️**")
    await typew.edit("**Vicky Peler✅**")
    sleep(1)
    await typew.edit("**Toni Gilaa☑️**")
    await typew.edit("**Toni Gilaa✅**")
    sleep(2)
    await typew.edit("**Karina Depresi☑️**")
    await typew.edit("**Karina Depresi✅**")
    sleep(2)
    await typew.edit("**Yunus Gajelas☑️**")
    await typew.edit("**Yunus Gajelas✅**")
    sleep(2)
    await typew.edit("**Adel GJM!☑️**")
    await typew.edit("**Adel GJM!✅**")
    sleep(2)
    await typew.edit("**Jia GJB!☑️**")
    await typew.edit("**Jia GJB!✅**")
    sleep(2)
    await typew.edit("**Imeh,MengRibet☑️**")
    await typew.edit("**Imeh,MengRibet✅**")
    sleep(2)
    await typew.edit("**Jeje,Mengintil☑️**")
    await typew.edit("**Jeje,Mengintil✅**")
    sleep(3)
    await typew.edit("**CUMA RAMA YANG BENER!**")


@register(outgoing=True, pattern='^.hapis(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Hapis,itu ganteng`")
    sleep(1)
    await typew.edit("`Anaknya baik`")
    sleep(1)
    await typew.edit("`Makanya kalo udah sama apis jan di sia siain tolo,apis limitid edition`")
    sleep(1)
    await typew.edit("`apis setia kok orangnya beneran dah,jan di sia siain dia!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, GC nya tante wina keren`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok banyak badut`")
    sleep(2)
    await typew.edit("`Oh iya, Kan banyak badut 🤡`")
    sleep(2)
    await typew.edit("`Kasian mau aja jadi badutnya si wina`")
    sleep(2)
    await typew.edit("`Kasian banget iduplu dah.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡,mending sama apis, Wkwkwk`")
    sleep(3)
    await typew.edit("`Kalo sama apis bakal di jadiin kaya ratu kok`")

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})
