# Mock external services with comprehensive test data

# User ID mapping for name lookups
USER_NAME_TO_ID = {
    "ana": "user_001",
    "Ana": "user_001",
    "sarah": "user_002",
    "Sarah": "user_002",
    "james": "user_003",
    "James": "user_003",
    "priya": "user_004",
    "Priya": "user_004",
    "marco": "user_005",
    "Marco": "user_005",
}

def get_user_profile(user_id: str) -> dict:
    """Fetch user profile from external service (mocked)."""
    # Try to resolve name to user_id if needed
    resolved_id = USER_NAME_TO_ID.get(user_id, user_id)
    
    mock_data = {
        "user_001": {
            "name": "Ana Müller",
            "email": "ana.muller@tech.com",
            "location": "Berlin, Germany",
            "joined": "2022-03-15",
            "bio": "AI/ML enthusiast and data scientist",
            "website": "https://ana-tech.blog",
            "company": "TechCorp Berlin"
        },
        "user_002": {
            "name": "Sarah Chen",
            "email": "sarah.chen@startups.io",
            "location": "San Francisco, USA",
            "joined": "2021-07-22",
            "bio": "Startup founder, investor, and tech writer",
            "website": "https://sarahwritestech.com",
            "company": "NextGen Ventures"
        },
        "user_003": {
            "name": "James Wilson",
            "email": "james.wilson@devops.pro",
            "location": "London, UK",
            "joined": "2020-11-10",
            "bio": "DevOps engineer and cloud architect",
            "website": "https://jameswilson-cloud.dev",
            "company": "CloudScale Ltd"
        },
        "user_004": {
            "name": "Priya Sharma",
            "email": "priya.sharma@webdev.com",
            "location": "Bangalore, India",
            "joined": "2023-01-05",
            "bio": "Full-stack developer and open source contributor",
            "website": "https://priya-codes.dev",
            "company": "IndiaStack Solutions"
        },
        "user_005": {
            "name": "Marco Rossi",
            "email": "marco.rossi@design.studio",
            "location": "Milan, Italy",
            "joined": "2021-05-18",
            "bio": "UI/UX designer and design systems advocate",
            "website": "https://marcodesigns.it",
            "company": "Design Studio Italia"
        }
    }
    return mock_data.get(resolved_id, {"error": f"User not found: {user_id}"})

def get_user_stats(user_id: str) -> dict:
    """Fetch user statistics from external service (mocked)."""
    # Try to resolve name to user_id if needed
    resolved_id = USER_NAME_TO_ID.get(user_id, user_id)
    
    mock_stats = {
        "user_001": {
            "posts": 142,
            "followers": 3840,
            "following": 521,
            "engagement_rate": 12.3,
            "total_likes": 18420,
            "average_comments_per_post": 5.2
        },
        "user_002": {
            "posts": 287,
            "followers": 12500,
            "following": 340,
            "engagement_rate": 18.7,
            "total_likes": 89630,
            "average_comments_per_post": 8.9
        },
        "user_003": {
            "posts": 95,
            "followers": 2100,
            "following": 687,
            "engagement_rate": 9.5,
            "total_likes": 8940,
            "average_comments_per_post": 3.7
        },
        "user_004": {
            "posts": 201,
            "followers": 7320,
            "following": 412,
            "engagement_rate": 15.2,
            "total_likes": 35680,
            "average_comments_per_post": 6.8
        },
        "user_005": {
            "posts": 163,
            "followers": 5640,
            "following": 502,
            "engagement_rate": 14.1,
            "total_likes": 22950,
            "average_comments_per_post": 5.9
        }
    }
    return mock_stats.get(resolved_id, {"error": f"Stats not found: {user_id}"})

def get_recent_activity(user_id: str, limit: int = 5) -> list:
    """Fetch recent activity from external service (mocked)."""
    # Try to resolve name to user_id if needed
    resolved_id = USER_NAME_TO_ID.get(user_id, user_id)
    
    mock_activity = {
        "user_001": [
            {"date": "2026-02-09", "action": "Published article: 'Deep Learning Trends 2026'", "type": "post", "engagement": 342},
            {"date": "2026-02-08", "action": "Attended: Advanced ML Techniques Workshop", "type": "event", "attendees": 256},
            {"date": "2026-02-07", "action": "Collaborated on: Open Source ML Library", "type": "collaboration", "contributors": 12},
            {"date": "2026-02-06", "action": "Shared: Data Science Best Practices Guide", "type": "post", "engagement": 289},
            {"date": "2026-02-05", "action": "Updated profile and portfolio", "type": "profile_update", "sections": 3}
        ],
        "user_002": [
            {"date": "2026-02-09", "action": "Posted: Startup Funding Tips for 2026", "type": "post", "engagement": 1240},
            {"date": "2026-02-08", "action": "Hosted webinar: Scaling Your Startup", "type": "event", "attendees": 842},
            {"date": "2026-02-07", "action": "Published: Monthly Tech Newsletter #47", "type": "newsletter", "subscribers": 5420},
            {"date": "2026-02-06", "action": "Launched: New Mentoring Program", "type": "initiative", "mentees": 23},
            {"date": "2026-02-04", "action": "Announced: Investment in 3 Early-Stage Startups", "type": "announcement", "amount": "$2.5M"}
        ],
        "user_003": [
            {"date": "2026-02-09", "action": "Deployed: Kubernetes Multi-Cluster Setup", "type": "technical", "systems": 15},
            {"date": "2026-02-08", "action": "Published: DevOps Architecture Patterns", "type": "post", "engagement": 198},
            {"date": "2026-02-07", "action": "Contributed to: Terraform Provider Project", "type": "open_source", "pr_merged": 4},
            {"date": "2026-02-06", "action": "Spoke at: Cloud Architecture Conference", "type": "event", "audience": 320},
            {"date": "2026-02-05", "action": "Released: Container Optimization Guide v2.0", "type": "publication", "downloads": 8420}
        ],
        "user_004": [
            {"date": "2026-02-09", "action": "Launched: New Web Framework Release", "type": "technical", "version": "4.2.0"},
            {"date": "2026-02-08", "action": "Posted: React Performance Optimization Tips", "type": "post", "engagement": 521},
            {"date": "2026-02-07", "action": "Hackathon Participation: Won 1st Place", "type": "event", "prize": "$5000"},
            {"date": "2026-02-06", "action": "Published: Full-Stack Development Guide", "type": "guide", "chapters": 18},
            {"date": "2026-02-05", "action": "Reviewed: 25 Code Contributions", "type": "open_source", "projects": 8}
        ],
        "user_005": [
            {"date": "2026-02-09", "action": "Unveiled: New Design System v3.0", "type": "design", "components": 240},
            {"date": "2026-02-08", "action": "Posted: UX Trends in 2026", "type": "post", "engagement": 634},
            {"date": "2026-02-07", "action": "Conducted: Design Workshop for Teams", "type": "event", "participants": 85},
            {"date": "2026-02-06", "action": "Published: Design Thinking Case Study", "type": "article", "views": 12500},
            {"date": "2026-02-05", "action": "Released: Figma Plugin for Accessibility", "type": "tool", "installs": 2340}
        ]
    }
    return mock_activity.get(resolved_id, [])

# Tool definitions for LangChain
TOOLS = [
    {
        "name": "get_user_profile",
        "description": "Get user profile information including name, email, location, and join date",
        "func": get_user_profile
    },
    {
        "name": "get_user_stats",
        "description": "Get user statistics like posts count, followers, and engagement rate",
        "func": get_user_stats
    },
    {
        "name": "get_recent_activity",
        "description": "Get recent activity of a user",
        "func": get_recent_activity
    }
]