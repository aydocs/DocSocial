#!/usr/bin/env python3
"""
🕵️ DocsSocial - Advanced OSINT Intelligence Suite
Creator: aydocs
Project: DocsSocial

A beautiful and powerful OSINT tool for Termux that collects intelligence from multiple sources
using phone numbers, usernames, emails, and profile pictures.

ETHICAL WARNING:
- This tool only collects publicly available information
- No hacking, brute-force, or illegal activities
- For educational and security research purposes only
- Users are responsible for ethical usage
"""

import requests
import json
import time
import re
import os
import shutil
from datetime import datetime, timedelta
from urllib.parse import urljoin, quote, urlparse
import sys
import argparse
from colorama import init, Fore, Style, Back
from bs4 import BeautifulSoup
import concurrent.futures
import random
import string
import hashlib
import base64
from PIL import Image
import io
import urllib.request
from bs4.element import Tag
import time
import calendar
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import threading

init(autoreset=True)
console = Console()

# Animated colorful banner
BANNER_COLORS = [Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.RED]
def animated_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    figlet = Figlet(font='slant')
    banner_text = "DocsSocial"
    for i in range(2):
        for color in BANNER_COLORS:
            print(color + figlet.renderText(banner_text))
            print(Fore.YELLOW + Style.BRIGHT + "🕵️ Advanced OSINT Intelligence Suite - by aydocs\n")
            print(Fore.MAGENTA + "🌟 Only collects publicly available information!\n" + Style.RESET_ALL)
            time.sleep(0.12)
            os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.CYAN + figlet.renderText(banner_text))
    print(Fore.YELLOW + Style.BRIGHT + "🕵️ Advanced OSINT Intelligence Suite - by aydocs\n")
    print(Fore.MAGENTA + "🌟 Only collects publicly available information!\n" + Style.RESET_ALL)

# Animated menu
MENU_OPTIONS = [
    ("👤 Username Intelligence (Detailed)", "username"),
    ("📱 Phone Number Intelligence", "phone"),
    ("📧 Email Intelligence", "email"),
    ("🖼️ Reverse Image Search", "photo"),
    ("🎯 Quick Username Search", "quick_username"),
    ("📊 Comprehensive Analysis", "analysis"),
    ("🚪 Exit", "exit")
]

def animated_menu():
    console.print("[bold yellow]Select your intelligence gathering method:[/bold yellow]\n")
    for idx, (desc, _) in enumerate(MENU_OPTIONS, 1):
        console.print(f"[bold cyan]{idx}.[/bold cyan] [white]{desc}[/white]")
        time.sleep(0.08)
    print()
    while True:
        try:
            choice = int(input(Fore.CYAN + Style.BRIGHT + "Select option (1-7): " + Style.RESET_ALL).strip())
            if 1 <= choice <= len(MENU_OPTIONS):
                return MENU_OPTIONS[choice-1][1]
            else:
                print(Fore.RED + "Invalid choice! Please select a valid option.")
        except ValueError:
            print(Fore.RED + "Please enter a number.")

# Loading animation
def loading_animation(task_desc="Processing"):
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), transient=True) as progress:
        task = progress.add_task(f"{task_desc}...", total=None)
        for _ in range(random.randint(15, 30)):
            time.sleep(0.07)
        progress.remove_task(task)

class DocsSocial:
    def __init__(self):
        self.session = requests.Session()
        self.setup_session()
        self.target = ''
        self.target_type = ''  # phone, username, email, photo
        self.results = {}
        self.found_data = {}
        self.verbose = False
        self.output_dir = ''
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def setup_session(self):
        """Advanced session configuration with anti-detection"""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        
        self.session.headers.update({
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,tr;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        })

    def print_status(self, message, status="info"):
        colors = {"info": Fore.BLUE, "success": Fore.GREEN, "warning": Fore.YELLOW, "error": Fore.RED}
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{colors.get(status, Fore.WHITE)}[{timestamp}] {message}")

    def create_output_structure(self):
        """Create organized output directory structure"""
        base_dir = f"docsocial_results_{self.target}_{self.timestamp}"
        self.output_dir = base_dir
        
        # Create main directories
        directories = [
            "social_media",
            "personal_info", 
            "images",
            "documents",
            "reports",
            "raw_data",
            "detailed_analysis"
        ]
        
        for dir_name in directories:
            os.makedirs(os.path.join(base_dir, dir_name), exist_ok=True)
        
        # Create subdirectories for social media
        social_platforms = ["instagram", "twitter", "facebook", "linkedin", "tiktok", "youtube", "github", "reddit"]
        for platform in social_platforms:
            os.makedirs(os.path.join(base_dir, "social_media", platform), exist_ok=True)
        
        self.print_status(f"📁 Created output directory: {base_dir}", "success")

    def extract_instagram_detailed_data(self, soup, username):
        """Extract detailed Instagram data including activity, creation time, etc."""
        data = {}
        
        # Check for private account
        if 'This Account is Private' in str(soup):
            data['is_private'] = True
            data['status'] = 'Private Account'
            return data
        
        data['is_private'] = False
        
        # Extract follower info from og:description
        og_desc = soup.find('meta', {'property': 'og:description'})
        if og_desc:
            content = og_desc.get('content', '')
            
            # Extract numbers with regex
            follower_match = re.search(r'([\d,]+) Followers', content)
            if follower_match:
                data['followers'] = follower_match.group(1)
            
            following_match = re.search(r'([\d,]+) Following', content)
            if following_match:
                data['following'] = following_match.group(1)
            
            posts_match = re.search(r'([\d,]+) Posts', content)
            if posts_match:
                data['posts'] = posts_match.group(1)
        
        # Extract bio and name
        og_title = soup.find('meta', {'property': 'og:title'})
        if og_title:
            data['display_name'] = og_title.get('content', '')
        
        # Check for verified account
        if 'Verified' in str(soup):
            data['is_verified'] = True
        else:
            data['is_verified'] = False
        
        # Try to extract account creation time from various sources
        try:
            # Look for JSON-LD data
            scripts = soup.find_all('script', type='application/ld+json')
            for script in scripts:
                try:
                    json_data = json.loads(script.string)
                    if isinstance(json_data, dict) and json_data.get('@type') == 'Person':
                        data['name'] = json_data.get('name', '')
                        data['description'] = json_data.get('description', '')
                        break
                except:
                    continue
            
            # Look for additional metadata
            meta_tags = soup.find_all('meta')
            for meta in meta_tags:
                if meta.get('property') == 'og:site_name':
                    data['platform'] = meta.get('content', '')
                elif meta.get('property') == 'og:url':
                    data['profile_url'] = meta.get('content', '')
        except Exception as e:
            data['extraction_error'] = str(e)
        
        return data

    def extract_twitter_detailed_data(self, soup, username):
        """Extract detailed Twitter data including activity, creation time, etc."""
        data = {}
        
        # Check for protected account
        if 'This account is protected' in str(soup):
            data['is_protected'] = True
            data['status'] = 'Protected Account'
            return data
        
        data['is_protected'] = False
        
        # Extract profile information
        title = soup.find('title')
        if title:
            title_text = title.text.strip()
            data['title'] = title_text
            
            # Try to extract display name from title
            if '(@' in title_text:
                display_name = title_text.split('(@')[0].strip()
                data['display_name'] = display_name
        
        # Check for verified account
        if 'Verified' in str(soup):
            data['is_verified'] = True
        else:
            data['is_verified'] = False
        
        # Try to extract bio
        meta_desc = soup.find('meta', {'name': 'description'})
        if meta_desc:
            data['bio'] = meta_desc.get('content', '')
        
        # Look for JSON-LD data for more details
        scripts = soup.find_all('script', type='application/ld+json')
        for script in scripts:
            try:
                json_data = json.loads(script.string)
                if isinstance(json_data, dict):
                    if json_data.get('@type') == 'Person':
                        data['name'] = json_data.get('name', '')
                        data['description'] = json_data.get('description', '')
                    elif json_data.get('@type') == 'Organization':
                        data['organization'] = json_data.get('name', '')
            except:
                continue
        
        return data

    def extract_github_detailed_data(self, soup, username):
        """Extract detailed GitHub data including activity, creation time, etc."""
        data = {}
        
        # Extract from JSON-LD data
        scripts = soup.find_all('script', type='application/ld+json')
        for script in scripts:
            try:
                json_data = json.loads(script.string)
                if isinstance(json_data, dict) and json_data.get('@type') == 'Person':
                    data['name'] = json_data.get('name', '')
                    data['description'] = json_data.get('description', '')
                    data['url'] = json_data.get('url', '')
                    break
            except:
                continue
        
        # Extract additional metadata
        meta_tags = soup.find_all('meta')
        for meta in meta_tags:
            if meta.get('property') == 'og:description':
                data['bio'] = meta.get('content', '')
            elif meta.get('property') == 'og:title':
                data['title'] = meta.get('content', '')
        
        return data

    def search_github_api_detailed(self, username):
        """Search GitHub profile using API with detailed information"""
        try:
            url = f'https://api.github.com/users/{username}'
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                
                # Calculate account age
                created_at = data.get('created_at', '')
                if created_at:
                    created_date = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
                    current_date = datetime.now()
                    account_age = current_date - created_date
                    data['account_age_days'] = account_age.days
                    data['account_age_years'] = account_age.days / 365.25
                    data['created_date_formatted'] = created_date.strftime('%Y-%m-%d %H:%M:%S')
                
                # Calculate activity metrics
                public_repos = data.get('public_repos', 0)
                followers = data.get('followers', 0)
                following = data.get('following', 0)
                
                data['activity_score'] = public_repos + followers + following
                data['engagement_ratio'] = followers / (following + 1) if following > 0 else followers
                
                # Add additional analysis
                data['profile_completeness'] = sum([
                    1 if data.get('name') else 0,
                    1 if data.get('bio') else 0,
                    1 if data.get('location') else 0,
                    1 if data.get('company') else 0,
                    1 if data.get('blog') else 0
                ]) / 5 * 100
                
                return data
            else:
                return None
                
        except Exception as e:
            return {'error': str(e)}

    def search_reddit_detailed(self, username):
        """Search Reddit profile with detailed information"""
        try:
            url = f'https://www.reddit.com/user/{username}/'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            response = self.session.get(url, timeout=15, headers=headers)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                
                data = {
                    'url': url,
                    'status': 'Found',
                    'scraped_at': datetime.now().isoformat()
                }
                
                # Extract title
                title = soup.find('title')
                if title:
                    data['title'] = title.text.strip()
                
                # Try to extract karma and other metrics
                karma_pattern = r'(\d+(?:,\d+)*)\s*karma'
                karma_match = re.search(karma_pattern, str(soup))
                if karma_match:
                    data['karma'] = karma_match.group(1)
                
                # Look for account age
                age_pattern = r'(\d+)\s*(?:years?|months?|days?)\s*old'
                age_match = re.search(age_pattern, str(soup))
                if age_match:
                    data['account_age'] = age_match.group(1)
                
                return data
            else:
                return None
                
        except Exception as e:
            return {'error': str(e)}

    def search_social_media_by_username(self, username):
        """Search username across social media platforms with detailed extraction"""
        platforms = [
            ('instagram', 'Instagram', '📸', f'https://www.instagram.com/{username}/'),
            ('twitter', 'Twitter/X', '🐦', f'https://twitter.com/{username}'),
            ('facebook', 'Facebook', '📘', f'https://www.facebook.com/{username}'),
            ('linkedin', 'LinkedIn', '💼', f'https://www.linkedin.com/in/{username}/'),
            ('tiktok', 'TikTok', '🎵', f'https://www.tiktok.com/@{username}'),
            ('youtube', 'YouTube', '📺', f'https://www.youtube.com/@{username}'),
            ('reddit', 'Reddit', '🤖', f'https://www.reddit.com/user/{username}/'),
            ('github', 'GitHub', '💻', f'https://github.com/{username}'),
            ('snapchat', 'Snapchat', '👻', f'https://www.snapchat.com/add/{username}'),
            ('pinterest', 'Pinterest', '📌', f'https://www.pinterest.com/{username}/'),
            ('twitch', 'Twitch', '🎮', f'https://www.twitch.tv/{username}'),
            ('discord', 'Discord', '🎧', f'https://discord.com/users/{username}'),
            ('telegram', 'Telegram', '📱', f'https://t.me/{username}'),
            ('medium', 'Medium', '📝', f'https://medium.com/@{username}'),
            ('deviantart', 'DeviantArt', '🎨', f'https://www.deviantart.com/{username}'),
            ('flickr', 'Flickr', '📷', f'https://www.flickr.com/photos/{username}/'),
            ('vimeo', 'Vimeo', '🎬', f'https://vimeo.com/{username}'),
            ('dribbble', 'Dribbble', '🏀', f'https://dribbble.com/{username}'),
            ('behance', 'Behance', '🎨', f'https://www.behance.net/{username}'),
            ('soundcloud', 'SoundCloud', '🎵', f'https://soundcloud.com/{username}')
        ]
        
        results = {}
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_platform = {
                executor.submit(self.check_platform_detailed, platform_info): platform_info 
                for platform_info in platforms
            }
            
            for future in concurrent.futures.as_completed(future_to_platform):
                platform_info = future_to_platform[future]
                platform_key, platform_name, platform_icon, url = platform_info
                
                try:
                    result = future.result()
                    if result:
                        results[platform_key] = result
                        self.print_status(f"{platform_icon} {platform_name}: ✅ Found", "success")
                        
                        # Save platform-specific data
                        self.save_platform_data(platform_key, result)
                    else:
                        self.print_status(f"{platform_icon} {platform_name}: ❌ Not found", "warning")
                except Exception as e:
                    self.print_status(f"{platform_icon} {platform_name}: ❌ Error - {str(e)}", "error")
        
        return results

    def check_platform_detailed(self, platform_info):
        """Check if profile exists on a specific platform with detailed extraction"""
        platform_key, platform_name, platform_icon, url = platform_info
        
        try:
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                
                data = {
                    'platform': platform_name,
                    'url': url,
                    'status': 'Found',
                    'scraped_at': datetime.now().isoformat()
                }
                
                # Extract basic info
                title = soup.find('title')
                if title:
                    data['title'] = title.text.strip()
                
                # Extract meta description
                meta_desc = soup.find('meta', {'name': 'description'})
                if isinstance(meta_desc, Tag) and 'content' in meta_desc.attrs:
                    data['description'] = meta_desc.attrs['content']
                
                # Extract profile image
                og_image = soup.find('meta', {'property': 'og:image'})
                if isinstance(og_image, Tag) and 'content' in og_image.attrs:
                    data['profile_image'] = og_image.attrs['content']
                
                # Platform-specific detailed data extraction
                if platform_key == 'instagram':
                    data.update(self.extract_instagram_detailed_data(soup, url.split('/')[-2]))
                elif platform_key == 'twitter':
                    data.update(self.extract_twitter_detailed_data(soup, url.split('/')[-1]))
                elif platform_key == 'github':
                    data.update(self.extract_github_detailed_data(soup, url.split('/')[-1]))
                
                return data
            elif response.status_code == 404:
                return None
            else:
                return None
                
        except Exception as e:
            if self.verbose:
                self.print_status(f"{platform_name} error: {str(e)}", "error")
            return None

    def search_by_username(self, username):
        """Search by username across all platforms with detailed analysis"""
        self.print_status(f"🔍 Starting detailed username intelligence gathering: {username}", "info")
        
        results = {
            'username': username,
            'search_type': 'username',
            'timestamp': datetime.now().isoformat(),
            'sources': {}
        }
        
        # Social media platforms with detailed extraction
        social_results = self.search_social_media_by_username(username)
        results['sources']['social_media'] = social_results
        
        # GitHub search with detailed API
        github_results = self.search_github_api_detailed(username)
        results['sources']['github'] = github_results
        
        # Reddit search with detailed analysis
        reddit_results = self.search_reddit_detailed(username)
        results['sources']['reddit'] = reddit_results
        
        # Generate comprehensive analysis
        results['analysis'] = self.generate_comprehensive_analysis(results)
        
        return results

    def generate_comprehensive_analysis(self, results):
        """Generate comprehensive analysis of all collected data"""
        analysis = {
            'total_platforms_found': 0,
            'verification_status': 'Unknown',
            'activity_level': 'Unknown',
            'social_presence_score': 0,
            'account_ages': [],
            'engagement_metrics': {},
            'risk_assessment': 'Low',
            'recommendations': []
        }
        
        social_data = results.get('sources', {}).get('social_media', {})
        analysis['total_platforms_found'] = len(social_data)
        
        # Calculate social presence score
        score = 0
        verified_count = 0
        total_followers = 0
        
        for platform, data in social_data.items():
            if data:
                score += 10  # Base score for each platform
                
                if data.get('is_verified'):
                    verified_count += 1
                    score += 20
                
                if data.get('followers'):
                    try:
                        followers = int(data['followers'].replace(',', ''))
                        total_followers += followers
                        if followers > 10000:
                            score += 30
                        elif followers > 1000:
                            score += 20
                        elif followers > 100:
                            score += 10
                    except:
                        pass
        
        analysis['social_presence_score'] = score
        analysis['total_followers'] = total_followers
        analysis['verified_accounts'] = verified_count
        
        # Determine activity level
        if score > 100:
            analysis['activity_level'] = 'Very High'
        elif score > 70:
            analysis['activity_level'] = 'High'
        elif score > 40:
            analysis['activity_level'] = 'Medium'
        elif score > 20:
            analysis['activity_level'] = 'Low'
        else:
            analysis['activity_level'] = 'Very Low'
        
        # Generate recommendations
        if verified_count > 0:
            analysis['recommendations'].append("✅ User has verified accounts - likely legitimate")
        
        if total_followers > 10000:
            analysis['recommendations'].append("🌟 High follower count - significant social influence")
        
        if len(social_data) > 10:
            analysis['recommendations'].append("📱 Extensive social media presence")
        
        return analysis

    def save_platform_data(self, platform, data):
        """Save platform-specific data to organized folders"""
        try:
            # Save to social_media folder
            platform_dir = os.path.join(self.output_dir, "social_media", platform)
            os.makedirs(platform_dir, exist_ok=True)
            
            # Save JSON data
            with open(os.path.join(platform_dir, f"{platform}_data.json"), 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Download profile image if available
            if data.get('profile_image'):
                try:
                    img_response = self.session.get(data['profile_image'], timeout=10)
                    if img_response.status_code == 200:
                        img_path = os.path.join(platform_dir, f"{platform}_profile.jpg")
                        with open(img_path, 'wb') as f:
                            f.write(img_response.content)
                        data['profile_image_saved'] = img_path
                        
                        # Also save to images folder
                        images_dir = os.path.join(self.output_dir, "images")
                        os.makedirs(images_dir, exist_ok=True)
                        img_copy_path = os.path.join(images_dir, f"{platform}_profile.jpg")
                        shutil.copy2(img_path, img_copy_path)
                except Exception as e:
                    data['profile_image_error'] = str(e)
            
            # Save HTML snapshot
            if data.get('url'):
                try:
                    response = self.session.get(data['url'], timeout=15)
                    if response.status_code == 200:
                        html_path = os.path.join(platform_dir, f"{platform}_page.html")
                        with open(html_path, 'w', encoding='utf-8') as f:
                            f.write(response.text)
                        data['html_saved'] = html_path
                        
                        # Also save to documents folder
                        docs_dir = os.path.join(self.output_dir, "documents")
                        os.makedirs(docs_dir, exist_ok=True)
                        doc_copy_path = os.path.join(docs_dir, f"{platform}_page.html")
                        shutil.copy2(html_path, doc_copy_path)
                except Exception as e:
                    data['html_error'] = str(e)
                    
        except Exception as e:
            self.print_status(f"Error saving {platform} data: {str(e)}", "error")

    def save_personal_info(self, results):
        """Save personal information to personal_info folder"""
        try:
            personal_dir = os.path.join(self.output_dir, "personal_info")
            os.makedirs(personal_dir, exist_ok=True)
            
            # Extract personal information from results
            personal_data = {
                'target': self.target,
                'target_type': self.target_type,
                'search_timestamp': datetime.now().isoformat(),
                'personal_details': {},
                'contact_info': {},
                'social_summary': {}
            }
            
            # Extract personal details from social media
            social_data = results.get('sources', {}).get('social_media', {})
            for platform, data in social_data.items():
                if data:
                    if data.get('display_name'):
                        personal_data['personal_details'][f'{platform}_name'] = data['display_name']
                    if data.get('bio'):
                        personal_data['personal_details'][f'{platform}_bio'] = data['bio']
                    if data.get('description'):
                        personal_data['personal_details'][f'{platform}_description'] = data['description']
                    if data.get('url'):
                        personal_data['contact_info'][f'{platform}_url'] = data['url']
                    if data.get('followers'):
                        personal_data['social_summary'][f'{platform}_followers'] = data['followers']
                    if data.get('following'):
                        personal_data['social_summary'][f'{platform}_following'] = data['following']
                    if data.get('posts'):
                        personal_data['social_summary'][f'{platform}_posts'] = data['posts']
            
            # Save personal info JSON
            with open(os.path.join(personal_dir, "personal_info.json"), 'w', encoding='utf-8') as f:
                json.dump(personal_data, f, indent=2, ensure_ascii=False)
            
            # Save contact details
            with open(os.path.join(personal_dir, "contact_details.json"), 'w', encoding='utf-8') as f:
                json.dump(personal_data['contact_info'], f, indent=2, ensure_ascii=False)
            
            # Save social summary
            with open(os.path.join(personal_dir, "social_summary.json"), 'w', encoding='utf-8') as f:
                json.dump(personal_data['social_summary'], f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.print_status(f"Error saving personal info: {str(e)}", "error")

    def save_detailed_analysis(self, results):
        """Save detailed analysis to detailed_analysis folder"""
        try:
            analysis_dir = os.path.join(self.output_dir, "detailed_analysis")
            os.makedirs(analysis_dir, exist_ok=True)
            
            # Extract analysis data
            analysis_data = results.get('analysis', {})
            
            # Save main analysis
            with open(os.path.join(analysis_dir, "analysis_report.json"), 'w', encoding='utf-8') as f:
                json.dump(analysis_data, f, indent=2, ensure_ascii=False)
            
            # Create detailed platform analysis
            platform_analysis = {}
            social_data = results.get('sources', {}).get('social_media', {})
            
            for platform, data in social_data.items():
                if data:
                    platform_analysis[platform] = {
                        'status': 'Found',
                        'verification': data.get('is_verified', False),
                        'privacy': 'Private' if data.get('is_private') else 'Public',
                        'followers': data.get('followers', 'N/A'),
                        'following': data.get('following', 'N/A'),
                        'posts': data.get('posts', 'N/A'),
                        'bio': data.get('bio', 'N/A'),
                        'title': data.get('title', 'N/A'),
                        'url': data.get('url', 'N/A')
                    }
            
            # Save platform analysis
            with open(os.path.join(analysis_dir, "platform_analysis.json"), 'w', encoding='utf-8') as f:
                json.dump(platform_analysis, f, indent=2, ensure_ascii=False)
            
            # Create risk assessment
            risk_assessment = {
                'target': self.target,
                'assessment_date': datetime.now().isoformat(),
                'risk_level': 'Low',
                'verification_score': 0,
                'social_presence_score': analysis_data.get('social_presence_score', 0),
                'activity_level': analysis_data.get('activity_level', 'Unknown'),
                'recommendations': analysis_data.get('recommendations', []),
                'flags': []
            }
            
            # Calculate verification score
            verified_count = analysis_data.get('verified_accounts', 0)
            total_platforms = analysis_data.get('total_platforms_found', 0)
            if total_platforms > 0:
                risk_assessment['verification_score'] = (verified_count / total_platforms) * 100
            
            # Determine risk level
            if verified_count > 0:
                risk_assessment['flags'].append("Has verified accounts")
            if analysis_data.get('social_presence_score', 0) > 100:
                risk_assessment['flags'].append("High social presence")
            if total_platforms > 10:
                risk_assessment['flags'].append("Extensive social footprint")
            
            # Save risk assessment
            with open(os.path.join(analysis_dir, "risk_assessment.json"), 'w', encoding='utf-8') as f:
                json.dump(risk_assessment, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.print_status(f"Error saving detailed analysis: {str(e)}", "error")

    def save_additional_documents(self, results):
        """Save additional documents to documents folder"""
        try:
            docs_dir = os.path.join(self.output_dir, "documents")
            os.makedirs(docs_dir, exist_ok=True)
            
            # Create executive summary
            summary = self.generate_summary()
            executive_summary = {
                'target': self.target,
                'search_type': self.target_type,
                'timestamp': datetime.now().isoformat(),
                'summary': summary,
                'key_findings': []
            }
            
            # Add key findings
            if summary['verified_accounts'] > 0:
                executive_summary['key_findings'].append(f"Found {summary['verified_accounts']} verified accounts")
            if summary['platforms_found'] > 5:
                executive_summary['key_findings'].append(f"Active on {summary['platforms_found']} platforms")
            if summary['profile_images_found'] > 0:
                executive_summary['key_findings'].append(f"Found {summary['profile_images_found']} profile images")
            
            # Save executive summary
            with open(os.path.join(docs_dir, "executive_summary.json"), 'w', encoding='utf-8') as f:
                json.dump(executive_summary, f, indent=2, ensure_ascii=False)
            
            # Create timeline report
            timeline = {
                'search_started': datetime.now().isoformat(),
                'platforms_checked': [],
                'findings': []
            }
            
            social_data = results.get('sources', {}).get('social_media', {})
            for platform, data in social_data.items():
                if data:
                    timeline['platforms_checked'].append({
                        'platform': platform,
                        'status': 'Found',
                        'url': data.get('url', ''),
                        'verification': data.get('is_verified', False),
                        'privacy': 'Private' if data.get('is_private') else 'Public'
                    })
                    timeline['findings'].append(f"Found {platform} profile: {data.get('url', '')}")
            
            # Save timeline
            with open(os.path.join(docs_dir, "timeline_report.json"), 'w', encoding='utf-8') as f:
                json.dump(timeline, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.print_status(f"Error saving additional documents: {str(e)}", "error")

    def generate_comprehensive_report(self):
        """Generate comprehensive OSINT report"""
        report = {
            'target': self.target,
            'target_type': self.target_type,
            'search_timestamp': datetime.now().isoformat(),
            'summary': self.generate_summary(),
            'detailed_results': self.results,
            'analysis': self.results.get('analysis', {})
        }
        
        # Save comprehensive report
        report_path = os.path.join(self.output_dir, "reports", "comprehensive_report.json")
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Save raw data
        raw_data_path = os.path.join(self.output_dir, "raw_data", "all_data.json")
        with open(raw_data_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        # Save data to all other folders
        self.save_personal_info(self.results)
        self.save_detailed_analysis(self.results)
        self.save_additional_documents(self.results)
        
        return report

    def generate_summary(self):
        """Generate summary of findings"""
        summary = {
            'total_platforms_checked': 0,
            'platforms_found': 0,
            'public_profiles': 0,
            'private_profiles': 0,
            'verified_accounts': 0,
            'profile_images_found': 0
        }
        
        if 'social_media' in self.results.get('sources', {}):
            social_data = self.results['sources']['social_media']
            summary['total_platforms_checked'] = len(social_data)
            summary['platforms_found'] = len([p for p in social_data.values() if p])
            
            for platform_data in social_data.values():
                if platform_data:
                    if platform_data.get('is_private'):
                        summary['private_profiles'] += 1
                    else:
                        summary['public_profiles'] += 1
                    
                    if platform_data.get('is_verified'):
                        summary['verified_accounts'] += 1
                    
                    if platform_data.get('profile_image'):
                        summary['profile_images_found'] += 1
        
        return summary

    def display_results(self):
        """Display comprehensive results with beautiful formatting"""
        print(f"\n{Fore.CYAN}{'='*80}")
        print(f"{Fore.YELLOW}📊 DocsSocial INTELLIGENCE REPORT")
        print(f"{Fore.CYAN}{'='*80}")
        
        print(f"{Fore.WHITE}🎯 Target: {Fore.GREEN}{self.target}")
        print(f"{Fore.WHITE}🔍 Search Type: {Fore.GREEN}{self.target_type.upper()}")
        print(f"{Fore.WHITE}📅 Search Date: {Fore.GREEN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Fore.WHITE}📁 Output Directory: {Fore.GREEN}{self.output_dir}")
        print(f"{Fore.CYAN}{'='*80}\n")
        
        # Summary section
        summary = self.generate_summary()
        print(f"{Fore.YELLOW}📋 EXECUTIVE SUMMARY:{Style.RESET_ALL}")
        print(f"   🔍 Platforms Checked: {Fore.GREEN}{summary['total_platforms_checked']}")
        print(f"   ✅ Profiles Found: {Fore.GREEN}{summary['platforms_found']}")
        print(f"   🔓 Public Profiles: {Fore.GREEN}{summary['public_profiles']}")
        print(f"   🔒 Private Profiles: {Fore.YELLOW}{summary['private_profiles']}")
        print(f"   ✅ Verified Accounts: {Fore.BLUE}{summary['verified_accounts']}")
        print(f"   🖼️ Profile Images: {Fore.GREEN}{summary['profile_images_found']}")
        print()
        
        # Analysis section
        analysis = self.results.get('analysis', {})
        if analysis:
            print(f"{Fore.YELLOW}📈 DETAILED ANALYSIS:{Style.RESET_ALL}")
            print(f"   🎯 Social Presence Score: {Fore.GREEN}{analysis.get('social_presence_score', 0)}")
            print(f"   📊 Activity Level: {Fore.GREEN}{analysis.get('activity_level', 'Unknown')}")
            print(f"   👥 Total Followers: {Fore.GREEN}{analysis.get('total_followers', 0):,}")
            print(f"   ✅ Verified Accounts: {Fore.BLUE}{analysis.get('verified_accounts', 0)}")
            print()
            
            if analysis.get('recommendations'):
                print(f"{Fore.YELLOW}💡 RECOMMENDATIONS:{Style.RESET_ALL}")
                for rec in analysis['recommendations']:
                    print(f"   {rec}")
                print()
        
        # Social media results
        if 'social_media' in self.results.get('sources', {}):
            social_data = self.results['sources']['social_media']
            if social_data:
                print(f"{Fore.YELLOW}📱 SOCIAL MEDIA FOOTPRINT:{Style.RESET_ALL}")
                
                for platform_key, data in social_data.items():
                    if data:
                        platform_name = data.get('platform', platform_key)
                        
                        # Status badge
                        if data.get('is_private'):
                            status_badge = f"{Back.YELLOW}{Fore.BLACK} PRIVATE {Style.RESET_ALL}"
                        elif data.get('is_verified'):
                            status_badge = f"{Back.BLUE}{Fore.WHITE} VERIFIED {Style.RESET_ALL}"
                        else:
                            status_badge = f"{Back.GREEN}{Fore.WHITE} PUBLIC {Style.RESET_ALL}"
                        
                        print(f"   {platform_name} {status_badge}")
                        print(f"      📍 URL: {data.get('url', 'N/A')}")
                        
                        if data.get('title'):
                            print(f"      📝 Title: {data.get('title')}")
                        
                        if data.get('description'):
                            print(f"      📄 Description: {data.get('description')}")
                        
                        if data.get('followers'):
                            print(f"      👥 Followers: {data.get('followers')}")
                        
                        if data.get('following'):
                            print(f"      👤 Following: {data.get('following')}")
                        
                        if data.get('posts'):
                            print(f"      📊 Posts: {data.get('posts')}")
                        
                        if data.get('profile_image'):
                            print(f"      🖼️ Profile Image: Available")
                        
                        print()
        
        # GitHub detailed results
        github_data = self.results.get('sources', {}).get('github', {})
        if github_data and not isinstance(github_data, dict):
            print(f"{Fore.YELLOW}🔍 GITHUB DETAILED RESULTS:{Style.RESET_ALL}")
            if isinstance(github_data, dict):
                for key, value in github_data.items():
                    if value and key not in ['status', 'note']:
                        print(f"   {key}: {value}")
            print()

    def run_interactive(self):
        """Run in interactive mode with beautiful UI"""
        animated_banner()
        
        print(f"{Fore.GREEN}🚀 Welcome to DocsSocial - Advanced OSINT Intelligence Suite!")
        print(f"{Fore.GREEN}Choose your intelligence gathering method:\n")
        
        selected = animated_menu()
        
        if selected == "exit":
            print(f"{Fore.YELLOW}👋 Goodbye!")
            return
        
        if selected == "username":
            username = input(f"{Fore.YELLOW}Enter username for detailed analysis: {Style.RESET_ALL}").strip()
            if username:
                self.target = username
                self.target_type = "username"
                self.create_output_structure()
                loading_animation("Searching across platforms")
                self.results = self.search_by_username(username)
        elif selected == "phone":
            phone = input(f"{Fore.YELLOW}Enter phone number: {Style.RESET_ALL}").strip()
            if phone:
                self.target = phone
                self.target_type = "phone"
                self.create_output_structure()
                loading_animation("Analyzing phone number")
                self.results = self.search_by_phone(phone)
        elif selected == "email":
            email = input(f"{Fore.YELLOW}Enter email address: {Style.RESET_ALL}").strip()
            if email:
                self.target = email
                self.target_type = "email"
                self.create_output_structure()
                loading_animation("Analyzing email")
                self.results = self.search_by_email(email)
        elif selected == "photo":
            photo_path = input(f"{Fore.YELLOW}Enter photo path: {Style.RESET_ALL}").strip()
            if photo_path and os.path.exists(photo_path):
                self.target = photo_path
                self.target_type = "photo"
                self.create_output_structure()
                loading_animation("Analyzing image")
                self.results = self.search_by_photo(photo_path)
            else:
                print(f"{Fore.RED}❌ Photo file not found!")
                return
        elif selected == "quick_username":
            username = input(f"{Fore.YELLOW}Enter username for quick search: {Style.RESET_ALL}").strip()
            if username:
                self.target = username
                self.target_type = "username"
                self.create_output_structure()
                loading_animation("Quick search")
                self.results = self.search_by_username(username)
        elif selected == "analysis":
            username = input(f"{Fore.YELLOW}Enter username for comprehensive analysis: {Style.RESET_ALL}").strip()
            if username:
                self.target = username
                self.target_type = "username"
                self.create_output_structure()
                loading_animation("Comprehensive analysis")
                self.results = self.search_by_username(username)
        
        # Generate and display results
        if self.results:
            self.generate_comprehensive_report()
            self.display_results()
            self.print_status(f"🎉 DocsSocial investigation completed! Results saved to: {self.output_dir}", "success")

    # Placeholder methods for other search types
    def search_by_phone(self, phone):
        """Search by phone number across multiple sources"""
        self.print_status(f"🔍 Starting phone number intelligence gathering: {phone}", "info")
        
        results = {
            'phone': phone,
            'search_type': 'phone_number',
            'timestamp': datetime.now().isoformat(),
            'sources': {}
        }
        
        # Phone number validation and formatting
        phone_clean = re.sub(r'[^\d+]', '', phone)
        if not phone_clean.startswith('+'):
            phone_clean = '+' + phone_clean
        
        results['formatted_phone'] = phone_clean
        
        # Basic phone number analysis
        phone_info = {
            'formatted_number': phone_clean,
            'country_code': phone_clean[:3] if len(phone_clean) > 3 else 'Unknown',
            'number_length': len(phone_clean.replace('+', '')),
            'is_valid_format': len(phone_clean.replace('+', '')) >= 10
        }
        
        results['sources']['phone_analysis'] = phone_info
        
        return results

    def search_by_email(self, email):
        """Search by email address"""
        self.print_status(f"🔍 Starting email intelligence gathering: {email}", "info")
        
        results = {
            'email': email,
            'search_type': 'email',
            'timestamp': datetime.now().isoformat(),
            'sources': {}
        }
        
        # Email validation and analysis
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid_email = re.match(email_pattern, email) is not None
        
        email_info = {
            'is_valid_format': is_valid_email,
            'domain': email.split('@')[1] if '@' in email else 'Invalid',
            'username': email.split('@')[0] if '@' in email else 'Invalid',
            'common_provider': email.split('@')[1] in ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'] if '@' in email else False
        }
        
        results['sources']['email_analysis'] = email_info
        
        return results

    def search_by_photo(self, photo_path):
        """Search by profile picture using reverse image search"""
        self.print_status(f"🔍 Starting photo intelligence gathering: {photo_path}", "info")
        
        results = {
            'photo_path': photo_path,
            'search_type': 'photo',
            'timestamp': datetime.now().isoformat(),
            'sources': {}
        }
        
        # Save image to output directory
        try:
            img_dir = os.path.join(self.output_dir, "images")
            shutil.copy2(photo_path, img_dir)
            results['sources']['image_saved'] = {'status': 'success', 'path': img_dir}
        except Exception as e:
            results['sources']['image_saved'] = {'error': str(e)}
        
        # Image analysis and metadata extraction
        try:
            with Image.open(photo_path) as img:
                img_info = {
                    'format': img.format,
                    'mode': img.mode,
                    'size': img.size,
                    'width': img.width,
                    'height': img.height
                }
                
                # Basic image information only
                results['sources']['image_analysis'] = img_info
                
        except Exception as e:
            results['sources']['image_analysis'] = {'error': str(e)}
        
        # Basic reverse image search using image hash
        try:
            import hashlib
            with open(photo_path, 'rb') as f:
                image_hash = hashlib.md5(f.read()).hexdigest()
            
            results['sources']['image_hash'] = {
                'md5_hash': image_hash,
                'file_size': os.path.getsize(photo_path),
                'note': 'Use this hash for reverse image search on platforms like TinEye, Google Images'
            }
        except Exception as e:
            results['sources']['image_hash'] = {'error': str(e)}
        
        return results

def main():
    # If no arguments provided, run interactive mode
    if len(sys.argv) == 1:
        tool = DocsSocial()
        tool.run_interactive()
        return
    
    parser = argparse.ArgumentParser(
        description="🕵️ DocsSocial - Advanced OSINT Intelligence Suite - Created by aydocs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python docsocial.py                    # Interactive mode
  python docsocial.py --username aydocs  # Username search
  python docsocial.py --phone +1234567890
  python docsocial.py --email user@example.com
  python docsocial.py --photo profile.jpg
        """
    )
    
    parser.add_argument('--username', help='Search by username')
    parser.add_argument('--phone', help='Search by phone number')
    parser.add_argument('--email', help='Search by email address')
    parser.add_argument('--photo', help='Search by profile picture')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode')
    
    args = parser.parse_args()
    
    tool = DocsSocial()
    tool.verbose = args.verbose
    
    if args.interactive:
        tool.run_interactive()
    elif args.username:
        tool.target = args.username
        tool.target_type = "username"
        tool.create_output_structure()
        tool.results = tool.search_by_username(args.username)
        tool.generate_comprehensive_report()
        tool.display_results()
    elif args.phone:
        tool.target = args.phone
        tool.target_type = "phone"
        tool.create_output_structure()
        tool.results = tool.search_by_phone(args.phone)
        tool.generate_comprehensive_report()
        tool.display_results()
    elif args.email:
        tool.target = args.email
        tool.target_type = "email"
        tool.create_output_structure()
        tool.results = tool.search_by_email(args.email)
        tool.generate_comprehensive_report()
        tool.display_results()
    elif args.photo:
        if os.path.exists(args.photo):
            tool.target = args.photo
            tool.target_type = "photo"
            tool.create_output_structure()
            tool.results = tool.search_by_photo(args.photo)
            tool.generate_comprehensive_report()
            tool.display_results()
        else:
            print(f"{Fore.RED}Error: Photo file not found!")
            sys.exit(1)
    else:
        print(f"{Fore.RED}Error: Please specify a search method or use --interactive!")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 