import discord
from discord.ext import commands
from discord import app_commands
import os

# 🔑 Token du bot depuis Replit secrets
TOKEN = os.environ['DISCORD_TOKEN']

# 🔹 Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 🔹 ID de ton serveur pour synchronisation rapide
GUILD_ID = 123456789012345678  # <- Remplace par ton serveur

# 🗂️ Dictionary des builds avec DM et salon images
builds = {
    "Byakuya Kuchiki": {
        "type": "Slash",
        "arme": "Senbonzakura",
        "accessoires": "Cloak, Spirit Ring",
        "strategie": "High-speed slash attacks with precision.",
        "dm_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869642452570122/Byakuya.png",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869642452570122/Byakuya.png"
    },

    "Gin Ichimaru": {
        "type": "Thrust",
        "arme": "Shinsō",
        "accessoires": "Crit Ring, Swift Cloak",
        "strategie": (
            "**__BUILDS__**\n"
            "- Weapon is a **must-have**\n"
            "- Core stamp is very strong (wait until the 16th)\n"
            "- Use **his own stamp set**\n\n"
            "**Slots:**\n"
            "- Slot 1: **ATK%** (Impale DMG) or **Thrust DMG Bonus**\n"
            "- Slot 2: **Crit Rate** (Crit DMG only if enough CR)\n"
            "- Slot 3: **Ailment DMG Bonus**\n\n"
            "**Substats:**\n"
            "- Crit Rate / Crit DMG\n"
            "- Ailment DMG\n"
            "- ATK%\n\n"
            "**NOTE:**\n"
            "- Gin bond requires **150% Ailment DMG**\n"
            "- 2pc stamp = 50%\n"
            "- Slot 3 max = 80%\n"
            "- Total = 130%, only **30% needed** (subs or Rangiku B2)\n\n"
            "**__BOUNDARIES__**\n"
            "- B1: Better rotations\n"
            "- B2: Huge Ultimate DMG\n"
            "- B4: Impale DMG boost\n"
            "- B6: Extra poison (strong but costly)\n\n"
            "**IMPORTANT:**\n"
            "Do NOT use ATK main stat on Slot 2 unless support DOT Gin.\n"
            "You lose damage on basics, skills, counter and ultimate."
        ),
        "dm_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1471327431028772915/EE7AB71B-3C9C-4757-8CEE-51404602D9DF.jpg",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869676807847947/image.png"
    },

    "Ichigo Kurosaki (Bankai)": {
        "type": "Slash",
        "arme": "Tensa Zangetsu",
        "accessoires": "Soul Cloak, Power Ring",
        "strategie": (
            "**Ichigo Kurosaki (Bankai) Build**\n"
            "**Type:** Slash\n"
            "**Weapon:** Tensa Zangetsu\n"
            "**Accessories:** Soul Cloak, Power Ring\n"
            "**Strategy:**\n"
            "• His weapon is a must have\n"
            "Effect: +15% Crit Rate. Special Attack summons 2 afterimages dealing 100% Special Attack DMG.\n"
            "• Core stamp: Getsuga Tangle (top-tier)\n"
            "• Use his own set stamp\n\n"
            "**Main stats:**\n"
            "• Slot 1: ATK% or Slash DMG\n"
            "• Slot 2: Crit DMG (Crit Rate is main build)\n"
            "• Slot 3: Ultimate Charge Rate\n\n"
            "**Substats:**\n"
            "• Crit Rate / Crit DMG / Ult Charge / ATK%\n\n"
            "**NOTE:**\n"
            "Each Special Attack during Hollowfication boosts next Deathblow by 15% (max 60%).\n\n"
            "**BOUNDARIES:**\n"
            "• B1: Better rotations\n"
            "• B2: Longer Getsuga Mark + DMG stacks\n"
            "• B6: DEMON (100% Special Attack DMG)"
        ),
        "dm_image": "https://cdn.discordapp.com/attachments/1471334537891024896/1471547831478386870/F8848097-6C3E-47DE-836F-D87A0B2006F0.jpg",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469879853112098837/image.png"
    },

    "Ikkaku Madarame": {
        "type": "Thrust",
        "arme": "Hōzukimaru",
        "accessoires": "Battle Cloak, Power Ring",
        "strategie": "Aggressive thrust attacks for sustained DPS.",
        "dm_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869687985803532/image.png",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869687985803532/image.png"
    },

    "Kaname Tosen": {
        "type": "Thrust",
        "arme": "Suzumushi",
        "accessoires": "Cloak, Spirit Ring",
        "strategie": "Focused attacks with crowd control.",
        "dm_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869708940546069/image.png",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869708940546069/image.png"
    },

    "Kenpachi Zaraki": {
        "type": "Slash",
        "arme": "Nozarashi",
        "accessoires": "Power Ring, Battle Cloak",
        "strategie": (
            "**__BUILDS__**\n"
            "- Weapon is **mandatory**\n"
            "- Core stamp is a must (A1 = **20% Crit Rate max**)\n"
            "- Use **his own stamp set**\n\n"
            "**Slots:**\n"
            "- Slot 1: **ATK%** or **Slash DMG Bonus**\n"
            "- Slot 2: **Crit Rate** (Crit DMG at B2)\n"
            "- Slot 3: **Ultimate Charge Rate**\n\n"
            "**Substats:**\n"
            "- Crit Rate / Crit DMG\n"
            "- Ultimate Charge Rate\n"
            "- Ailment DMG Bonus\n"
            "- ATK%\n\n"
            "**NOTE:**\n"
            "- Use **Tōshirō bond** for B0–B1\n"
            "- Use **Gin bond** for B2+\n\n"
            "**__BOUNDARIES__**\n"
            "- B1: Better rotations\n"
            "- B2: Crit buffs\n"
            "- B4: Overall DMG increase\n"
            "- B6: ABSOLUTE MONSTER"
        ),
        "dm_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1471329260814729319/365E3686-8879-4149-BF67-546A35C6CCB3.jpg",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869663134416946/image.png"
    },

    "Sosuke Aizen": {
        "type": "Spirit",
        "arme": "Kyoka Suigetsu",
        "accessoires": "Illusion Cloak, Mana Amulet",
        "strategie": (
            "Aim for **85% Crit Rate** (≈60% without weapon)\n"
            "and **100%+ Crit DMG**.\n\n"
            "- Stamp 1: **Spirit DMG%**\n\n"
            "**IMPORTANT:**\n"
            "- B6 doubles Crit Rate\n"
            "- Do NOT exceed 100% Crit Rate\n"
            "- Prioritize Crit DMG"
        ),
        "dm_image": "https://cdn.discordapp.com/attachments/1459536540094173376/1459536540257747119/0E3AF211-9A2A-45D2-8693-F744D5C4DEF5.jpg",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1470073623615115275/image.png"
    },

    "Toshiro Hitsugaya": {
        "type": "Spirit",
        "arme": "Hyorinmaru",
        "accessoires": "Frozen Cloak, Spirit Amulet",
        "strategie": (
            "**❄️ Tōshirō Hitsugaya — Bankai**\n\n"
            "**SSR Spirit DPS** focused on burst during **20s Bankai**\n\n"
            "**Build Priority:**\n"
            "- Crit Rate ➜ Crit DMG ➜ ATK\n"
            "- Weapon & Core are mandatory\n\n"
            "**Frozen Effect:**\n"
            "- **20–30% increased damage** to frozen enemies\n"
            "- Boosts Crit scaling\n"
            "- High Frozen uptime in Bankai\n\n"
            "**Why he’s strong:**\n"
            "- Massive burst\n"
            "- Insane Crit scaling\n"
            "- Constant Frozen ❄️"
        ),
        "dm_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1471328024921116888/46442179-D67E-4B3F-B2F3-850E5D74E9E8.jpg",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869698735804428/image.png"
    },

    "Yoruichi Shihouin": {
        "type": "Strike",
        "arme": "Shunkō",
        "accessoires": "Speed Cloak, Agility Ring",
        "strategie": "Fast melee strikes and extreme mobility.",
        "dm_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869629290844423/Yoruichi.png",
        "salon_image": "https://cdn.discordapp.com/attachments/1469712498482745589/1469869629290844423/Yoruichi.png"
    }
}

class BuildSelect(discord.ui.Select):
    def __init__(self, author_id: int):
        self.author_id = author_id
        options = [
            discord.SelectOption(label=name, description=f"View {name}'s build")
            for name in sorted(builds.keys())
        ]
        super().__init__(placeholder="Select a character...", options=options)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(
                "❌ You are not allowed to use this menu.",
                ephemeral=True
            )
            return

        personnage = self.values[0]
        build = builds[personnage]

        dm_embed = discord.Embed(
            title=f"💥 {personnage} Build",
            color=discord.Color.blue()
        )
        dm_embed.add_field(name="Type", value=build.get("type", "N/A"), inline=True)
        dm_embed.add_field(name="Weapon", value=build.get("arme", "N/A"), inline=True)
        dm_embed.add_field(name="Accessories", value=build.get("accessoires", "N/A"), inline=False)
        dm_embed.add_field(name="Strategy", value=build.get("strategie", "N/A"), inline=False)
        dm_embed.set_image(url=build.get("dm_image"))

        await interaction.response.send_message("✅ Check your DMs!", ephemeral=True)

        try:
            await interaction.user.send(embed=dm_embed)
        except discord.Forbidden:
            await interaction.followup.send(
                "❌ Your DMs are closed.",
                ephemeral=True
            )

        channel_embed = discord.Embed(
            title=f"📢 {personnage} Build",
            description="💬 Salon info ici",
            color=discord.Color.green()
        )
        channel_embed.set_image(url=build.get("salon_image"))
        await interaction.channel.send(embed=channel_embed)

class BuildView(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=60)
        self.add_item(BuildSelect(author_id))

# -------------------- COMMANDES --------------------
@bot.tree.command(name="builds", description="Voir les builds")
async def builds_slash(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"📢 {interaction.user.mention} is selecting a build!",
        view=BuildView(interaction.user.id),
        ephemeral=False
    )

# -------------------- READY --------------------

# -------------------- MAX SSR DATA --------------------

SSR_RESOURCES = {
    "spiritual_power_total": 6740,
    "daily_spiritual_power": 310,
    "kans": 4328450,
    "exp": 6347000,
    "omamori": 90,
    "stamp_ectoplasm": 2970,
    "stamp_nexus": 10
}

@bot.tree.command(
    name="max_ssr",
    description="Affiche les ressources nécessaires pour maxer un SSR"
)
async def max_ssr(interaction: discord.Interaction):
    days_needed = (
        SSR_RESOURCES["spiritual_power_total"]
        / SSR_RESOURCES["daily_spiritual_power"]
    )

    embed = discord.Embed(
        title="💀 Max SSR Ressources",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="🔋 SP total",
        value=SSR_RESOURCES["spiritual_power_total"],
        inline=True
    )
    embed.add_field(
        name="📅 SP / jour",
        value=SSR_RESOURCES["daily_spiritual_power"],
        inline=True
    )
    embed.add_field(
        name="⏳ Jours nécessaires",
        value=f"{days_needed:.1f} jours",
        inline=False
    )

    embed.add_field(
        name="💰 Kans total",
        value=f"{SSR_RESOURCES['kans']:,}",
        inline=True
    )
    embed.add_field(
        name="📘 EXP total",
        value=f"{SSR_RESOURCES['exp']:,}",
        inline=True
    )
    embed.add_field(
        name="🧿 Omamori",
        value=SSR_RESOURCES["omamori"],
        inline=True
    )
    embed.add_field(
        name="🧪 Stamp Ectoplasm",
        value=SSR_RESOURCES["stamp_ectoplasm"],
        inline=True
    )
    embed.add_field(
        name="🧬 Stamp Nexus",
        value=SSR_RESOURCES["stamp_nexus"],
        inline=True
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.event
async def on_ready():
    print(f'Bot connecté comme {bot.user}')
    try:
        synced = await bot.tree.sync()  # synchronise les commandes slash
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(e)

bot.run(TOKEN)
