# Discord Bot Template

This is a template for creating a Discord bot using Python and the `discord.py` library. The bot includes a simple command to repeat messages and is designed to be easily extended.

## Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `python-dotenv` library

## Setup

### Step 1: Clone the Repository

Clone this repository to your local machine:

```shell
git clone https://github.com/yourusername/discord-bot-template.git
cd discord-bot-template
```
### Step 2: Install Dependencies

Install the required libraries using pip: 

```shell
pip install discord.py python-dotenv
```

### Step 3: Configure the `.env` File

Create a `.env` file in the root directory of the project and add your bot token:

```shell
TOKEN=your-bot-token-here
```
Replace your-bot-token-here with the actual bot token you obtained from the [Discord Developer Portal](https://discord.com/developers/applications).

### Step 4: Enable Privileged Gateway Intents

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Select your bot application.
3. Navigate to the **"Bot"** tab.
4. Scroll down to the **Privileged Gateway Intents** section.
5. Enable the following intents:
   - **Presence Intent**
   - **Server Members Intent**
   - **Message Content Intent**

### Step 5: Run the Bot

Run the bot with the following command:

```shell
python your_bot_script.py
```

Replace `your_bot_script.py` with the name of your Python file containing the bot code.

## Usage

The template has one command already implemented that can be used right away. Once the bot is running, you can use the `/say` command in Discord to make the bot repeat any message.

**Example:**

```
/say Hello, world!
```

## Contributing

Feel free to contribute to this project by creating pull requests or opening issues.

## License

This project is open-source and available under the [MIT License](LICENSE).
