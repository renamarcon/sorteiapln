import feedparser
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

RSS_FEED_URL = 'https://omny.fm/shows/pauta-livre-news/playlists/podcast.rss'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("ALEGRIA! Bora sortear um episódio? Finge que é novo, vai!")

async def sortear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    feed = feedparser.parse(RSS_FEED_URL)
    episodes = feed.entries
    import random
    episode = random.choice(episodes)
    await update.message.reply_text(f"🐂 Ei macho! Tome teu episódio:\n{episode.title}\n{episode.link}")

def main() -> None:
    application = Application.builder().token("8030451194:AAFm19RnWBxUL6iL1fQSAyOnYZziEyCkld4").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("sortear", sortear))

    application.run_polling()

if __name__ == '__main__':
    main()