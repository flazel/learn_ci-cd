# Travenor

A full-fidelity travel application built with Flutter & Supabase.

## Features

- **Explore** — Browse destinations with images, ratings, and categories
- **Search** — Find destinations by name, location, or category
- **Favorites** — Bookmark destinations for later
- **Schedule** — Plan trips with date range, status tracking (Planning/Upcoming/Completed)
- **Previous Trips** — View completed trip history in your profile
- **Chat** — Real-time 1-on-1 messaging with other users
- **Profile** — Edit profile, upload avatar, manage account
- **Authentication** — Sign up, sign in, forgot password with Supabase Auth
- **Dark Mode** — Light/dark theme toggle
- **Multi-language** — English & Indonesian support

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Flutter (Dart) |
| State Management | Provider |
| Backend | Supabase (Auth, Database, Storage, Realtime) |
| Local DB | SQLite (sqflite) |
| Maps/Geocoding | Geoapify API |
| Images | CachedNetworkImage, FilePicker |
| Notifications | Local (in-app) |

## Getting Started

### Prerequisites

- Flutter SDK >=3.0.0
- A Supabase project (or use the existing one)

### Setup

```bash
# Clone & enter project
cd travenor

# Install dependencies
flutter pub get

# Create .env file
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key

# Run on web
flutter run -d chrome

# Run on Android (device with USB debugging)
flutter run
```

### Database Migrations

SQL migrations are in `supabase/migrations/`. Run them in order via the Supabase SQL Editor:

1. `00001_create_destinations.sql`
2. `00002_create_storage.sql`
3. `00003_create_comments.sql`
4. `00004_add_user_profile_image.sql`
5. `00005_create_schedules.sql`
6. `00006_add_notes_to_schedules.sql`
7. `00007_create_chat.sql`
8. `00008_add_unread.sql`
9. `00009_add_admin_role.sql`

### RPC Functions

The chat feature requires these PostgreSQL functions (defined in migrations 00007–00008):

- `get_conversations()` — List all conversations for the current user
- `get_or_create_conversation(other_user_id UUID)` — Find or create a 1-on-1 conversation
- `get_unread_count()` — Total unread messages
- `get_unread_count_for_conversation(conv_id UUID)` — Unread per conversation
- `mark_conversation_read(conv_id UUID)` — Mark conversation as read

### Database Triggers

- `on_auth_user_created` / `on_auth_user_updated` — Sync `auth.users` → `profiles` table

## Project Structure

```
lib/
├── components/         # Reusable UI widgets
├── config/             # Constants, theme, colors, text styles, language
├── data/
│   ├── database/       # SQLite helper
│   ├── models/         # Data models (banner only)
│   └── services/       # API services (Supabase + external)
├── models/             # Main data models
├── providers/          # State management providers
├── screens/            # App screens
│   ├── add_travel/
│   ├── auth/
│   ├── details/
│   ├── explore/
│   ├── home/
│   ├── messages/
│   ├── onboarding/
│   ├── profile/
│   ├── schedule/
│   ├── search/
│   ├── settings/
│   ├── splash/
│   └── main_wrapper/
└── main.dart           # App entry point
```

## Key Dependencies

- `supabase_flutter` — Auth, database, storage, realtime
- `provider` — State management
- `cached_network_image` — Image caching
- `file_picker` — Image selection
- `carousel_slider` — Banner carousel
- `sqflite` + `sqflite_common_ffi` — Local storage (desktop)
- `flutter_dotenv` — Environment variables
- `google_fonts` — Typography
