# 🕵️ DocsSocial - Advanced OSINT Intelligence Suite

<div align="center">

![DocsSocial Banner](https://img.shields.io/badge/DocsSocial-Advanced%20OSINT-blue?style=for-the-badge&logo=search)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Creator](https://img.shields.io/badge/Creator-aydocs-purple?style=for-the-badge)

**Created with 💜 by aydocs**

*A beautiful and powerful OSINT tool for collecting intelligence from multiple sources using phone numbers, usernames, emails, and profile pictures.*

</div>

---

## 🌟 Features

### 🔍 **Multi-Source Intelligence Gathering**
- **Username Search**: 20+ social media platforms
- **Phone Number Analysis**: Carrier detection, location analysis
- **Email Intelligence**: Domain analysis, breach checking
- **Reverse Image Search**: Profile picture analysis

### 📊 **Advanced Data Extraction**
- **Detailed Profile Information**: Followers, following, posts, bio
- **Account Verification Status**: Verified accounts detection
- **Activity Analysis**: Account age, activity level, engagement metrics
- **Privacy Status**: Public/private account detection

### 🎨 **Beautiful Terminal Interface**
- **ASCII Art Banner**: Professional DocsSocial branding with animations
- **Color-coded Output**: Easy-to-read status indicators
- **Interactive Menu**: User-friendly command selection with animations
- **Real-time Progress**: Live status updates and loading animations

### 📁 **Organized Output**
- **Structured Folders**: Social media, personal info, images, reports
- **JSON Reports**: Comprehensive data in structured format
- **HTML Snapshots**: Archived web pages
- **Profile Images**: Downloaded profile pictures

---

## 🚀 Installation & Usage

### 📱 **Termux (Android)**

#### Installation
```bash
pkg update && pkg upgrade
pkg install python git
pip install --upgrade pip

# Download project
cd ~
git clone https://github.com/aydocs/docsocial.git
cd docsocial/social-intel

# Install dependencies
pip install -r requirements.txt

# or use the auto-runner
bash run_docsocial.sh
```

#### Usage
```bash
# Interactive mode (Animated menu)
python docsocial.py

# Command line
python docsocial.py --username aydocs
python docsocial.py --phone +1234567890
python docsocial.py --email user@example.com
python docsocial.py --photo profile.jpg
```

### 🪟 **Windows**

#### Prerequisites
- Python 3.8 or higher
- Git for Windows

#### Installation
```powershell
# Install Python from https://python.org if not installed
# Install Git from https://git-scm.com if not installed

# Clone the repository
git clone https://github.com/aydocs/docsocial.git
cd docsocial/social-intel

# Install dependencies
pip install -r requirements.txt

# or use the Windows batch file
run_docsocial.bat
```

#### Usage
```powershell
# Interactive mode (Animated menu)
python docsocial.py

# Command line
python docsocial.py --username aydocs
python docsocial.py --phone +1234567890
python docsocial.py --email user@example.com
python docsocial.py --photo profile.jpg
```

### 🐧 **Linux (Ubuntu/Debian)**

#### Prerequisites
```bash
sudo apt update
sudo apt install python3 python3-pip git
```

#### Installation
```bash
# Clone the repository
git clone https://github.com/aydocs/docsocial.git
cd docsocial/social-intel

# Install dependencies
pip3 install -r requirements.txt

# or use the shell script
bash run_docsocial.sh
```

#### Usage
```bash
# Interactive mode (Animated menu)
python3 docsocial.py

# Command line
python3 docsocial.py --username aydocs
python3 docsocial.py --phone +1234567890
python3 docsocial.py --email user@example.com
python3 docsocial.py --photo profile.jpg
```

### 🍎 **macOS**

#### Prerequisites
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and Git
brew install python git
```

#### Installation
```bash
# Clone the repository
git clone https://github.com/aydocs/docsocial.git
cd docsocial/social-intel

# Install dependencies
pip3 install -r requirements.txt

# or use the shell script
bash run_docsocial.sh
```

#### Usage
```bash
# Interactive mode (Animated menu)
python3 docsocial.py

# Command line
python3 docsocial.py --username aydocs
python3 docsocial.py --phone +1234567890
python3 docsocial.py --email user@example.com
python3 docsocial.py --photo profile.jpg
```

### 🔧 **Quick Start (All Platforms)**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aydocs/docsocial.git
   cd docsocial/social-intel
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tool:**
   ```bash
   python docsocial.py
   ```

4. **Follow the interactive menu to start gathering intelligence!**



---

## 📸 Screenshots

### Animated Banner & Menu
```

  _____                 _____               _         _ 
 |  __ \               / ____|             (_)       | |
 | |  | |  ___    ___ | (___    ___    ___  _   __ _ | |
 | |  | | / _ \  / __| \___ \  / _ \  / __|| | / _` || |
 | |__| || (_) || (__  ____) || (_) || (__ | || (_| || |
 |_____/  \___/  \___||_____/  \___/  \___||_| \__,_||_|

🕵️ Advanced OSINT Intelligence Suite - by aydocs

🌟 Only collects publicly available information!

Select your intelligence gathering method:

1. 👤 Username Intelligence (Detailed)
2. 📱 Phone Number Intelligence
3. 📧 Email Intelligence
4. 🖼️ Reverse Image Search
5. 🎯 Quick Username Search
6. 📊 Comprehensive Analysis
7. 🚪 Exit
```

### Sample Results
```
================================================================================
📊 DocsSocial INTELLIGENCE REPORT
================================================================================
🎯 Target: aydocs
🔍 Search Type: USERNAME
📅 Search Date: 2025-07-06 02:23:34
📁 Output Directory: docsocial_results_aydocs_20250706_022317
================================================================================

📋 EXECUTIVE SUMMARY:
   🔍 Platforms Checked: 20
   ✅ Profiles Found: 11
   🔓 Public Profiles: 11
   🔒 Private Profiles: 0
   ✅ Verified Accounts: 1
   🖼️ Profile Images: 3

📈 DETAILED ANALYSIS:
   🎯 Social Presence Score: 130
   📊 Activity Level: Very High
   👥 Total Followers: 0
   ✅ Verified Accounts: 1

💡 RECOMMENDATIONS:
   ✅ User has verified accounts - likely legitimate
   📱 Extensive social media presence

📱 SOCIAL MEDIA FOOTPRINT:
   Instagram  PUBLIC 
      📍 URL: https://www.instagram.com/aydocs/
      👥 Followers: 1,234
      👤 Following: 567
      📊 Posts: 89
      🖼️ Profile Image: Available

   Twitter/X  VERIFIED 
      📍 URL: https://twitter.com/aydocs
      👥 Followers: 12,345
      🖼️ Profile Image: Available
```

---

## 📱 Supported Platforms

<div align="center">

<div align="center">

### Social Media Networks

<!-- Updated with medium/colored icons -->

<img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/instagram.svg" width="40" height="40" alt="Instagram" /> **Instagram** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/twitter-x.svg" width="40" height="40" alt="Twitter/X" /> **Twitter/X** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/facebook.svg" width="40" height="40" alt="Facebook" /> **Facebook** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/linkedin.svg" width="40" height="40" alt="LinkedIn" /> **LinkedIn** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/tiktok.svg" width="40" height="40" alt="TikTok" /> **TikTok** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/youtube.svg" width="40" height="40" alt="YouTube" /> **YouTube** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/reddit.svg" width="40" height="40" alt="Reddit" /> **Reddit** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/github.svg" width="40" height="40" alt="GitHub" /> **GitHub** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/snapchat.svg" width="40" height="40" alt="Snapchat" /> **Snapchat** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/pinterest.svg" width="40" height="40" alt="Pinterest" /> **Pinterest** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/twitch.svg" width="40" height="40" alt="Twitch" /> **Twitch** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/discord.svg" width="40" height="40" alt="Discord" /> **Discord** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/telegram.svg" width="40" height="40" alt="Telegram" /> **Telegram** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/medium.svg" width="40" height="40" alt="Medium" /> **Medium** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/deviantart.svg" width="40" height="40" alt="DeviantArt" /> **DeviantArt** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/flickr.svg" width="40" height="40" alt="Flickr" /> **Flickr** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/vimeo.svg" width="40" height="40" alt="Vimeo" /> **Vimeo** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/dribbble.svg" width="40" height="40" alt="Dribbble" /> **Dribbble** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/behance.svg" width="40" height="40" alt="Behance" /> **Behance** <img src="https://raw.githubusercontent.com/CLorant/readme-social-icons/main/medium/colored/soundcloud.svg" width="40" height="40" alt="SoundCloud" /> **SoundCloud**

</div>
### Additional Sources
📞 **Phone Carriers** - Carrier detection, location  
📧 **Email Providers** - Domain analysis, breach checking  
🖼️ **Image Analysis** - Metadata extraction, reverse search

</div>

---

## 📁 Output Structure

```
docsocial_results_[target]_[timestamp]/
├── social_media/
│   ├── instagram/
│   │   ├── instagram_data.json
│   │   ├── instagram_profile.jpg
│   │   └── instagram_page.html
│   ├── twitter/
│   ├── facebook/
│   └── ...
├── personal_info/
│   ├── personal_info.json
│   ├── contact_details.json
│   └── social_summary.json
├── images/
│   └── *_profile.jpg
├── documents/
│   ├── executive_summary.json
│   ├── timeline_report.json
│   └── *_page.html
├── reports/
│   └── comprehensive_report.json
├── raw_data/
│   └── all_data.json
└── detailed_analysis/
    ├── analysis_report.json
    ├── platform_analysis.json
    └── risk_assessment.json
```

---

## 🔧 Advanced Features

### Detailed Data Extraction
- **Account Age**: Creation date calculation
- **Activity Level**: Engagement metrics analysis
- **Social Presence Score**: Comprehensive scoring system
- **Verification Status**: Blue checkmark detection
- **Privacy Analysis**: Public/private account detection

### Anti-Detection Measures
- **Rotating User Agents**: Multiple browser signatures
- **Request Delays**: Rate limiting protection
- **Session Management**: Persistent connections
- **Error Handling**: Graceful failure recovery

### Comprehensive Analysis
- **Risk Assessment**: Automated threat evaluation
- **Recommendations**: Actionable intelligence insights
- **Engagement Metrics**: Follower/following ratios
- **Profile Completeness**: Data completeness scoring

---

## 🛡️ Ethical Usage

### ⚠️ Important Disclaimer
This tool is designed for **educational and security research purposes only**. 

### ✅ Permitted Uses
- **Security Research**: Vulnerability assessment
- **Digital Forensics**: Legal investigations
- **Social Media Analysis**: Public data gathering
- **Educational Purposes**: Learning OSINT techniques

### ❌ Prohibited Uses
- **Stalking or Harassment**: Personal targeting
- **Illegal Surveillance**: Unauthorized monitoring
- **Data Breaches**: Unauthorized access
- **Privacy Violations**: Non-consensual data collection

### 🔒 Privacy Protection
- Only collects **publicly available** information
- No password cracking or brute force attacks
- Respects robots.txt and rate limits
- No private account hacking

---

## 🛠️ Technical Details

### Dependencies
```python
requests>=2.28.0          # HTTP requests
beautifulsoup4>=4.11.0    # HTML parsing
colorama>=0.4.5           # Terminal colors
pillow>=9.0.0             # Image processing
lxml>=4.9.0               # XML/HTML parser
tqdm>=4.64.0              # Progress bars
pyfiglet>=0.8.0           # ASCII art
rich>=12.0.0              # Rich terminal output
```

### System Requirements
- **Python**: 3.8 or higher
- **OS**: Termux, Linux, macOS, Windows
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB free space
- **Network**: Internet connection required

### Performance
- **Concurrent Processing**: Up to 10 parallel requests
- **Response Time**: 2-5 seconds per platform
- **Memory Usage**: ~50MB during operation
- **Output Size**: 1-10MB per search

---

## 🚨 Troubleshooting

### Common Issues

**Python not found:**
```bash
# Termux
pkg install python

# Windows
python docsocial.py

# Linux/Mac
python3 docsocial.py
```

**Module not found:**
```bash
pip install -r requirements.txt
```

**Network errors:**
- Check internet connection
- Try with VPN
- Wait and retry

**Rate limiting:**
- Tool automatically handles delays
- Wait 1-2 minutes between searches

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
```bash
git clone [repository-url]
cd social-intel
pip install -r requirements.txt
python docsocial.py --interactive
```

---

## 📞 Support

- **Creator**: aydocs
- **Project**: DocsSocial
- **Version**: 2.0.0
- **Last Updated**: 2024

---

<div align="center">

**🌟 Star this project if you find it useful! 🌟**

*Built with 💜 for the OSINT community*

</div>