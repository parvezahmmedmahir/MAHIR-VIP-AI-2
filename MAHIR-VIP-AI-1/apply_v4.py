import re

# Read the HTML file
with open('INDEX.HTML', 'r', encoding='utf-8') as f:
    content = f.read()

# V4 Premium Container CSS
v4_container = '''        .container {
            max-width: 450px;
            width: 100%;
            background: linear-gradient(135deg, rgba(10, 14, 23, 0.85) 0%, rgba(5, 8, 15, 0.9) 100%);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 24px;
            padding: 30px;
            box-shadow: 
                0 8px 32px 0 rgba(0, 0, 0, 0.37),
                0 0 0 1px rgba(255, 215, 0, 0.1) inset,
                0 20px 60px rgba(255, 215, 0, 0.15);
            border: 1px solid rgba(255, 215, 0, 0.2);
            position: relative;
            overflow: hidden;
            transform-style: preserve-3d;
            perspective: 1000px;
        }

        .container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.6), transparent);
            z-index: 1;
        }

        .container::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 215, 0, 0.08) 0%, transparent 70%);
            animation: containerGlow 8s ease-in-out infinite;
            pointer-events: none;
            z-index: 0;
        }

        @keyframes containerGlow {
            0%, 100% {
                transform: translate(0, 0) scale(1);
                opacity: 0.5;
            }
            50% {
                transform: translate(10%, 10%) scale(1.1);
                opacity: 0.8;
            }
        }'''

# Find and replace the container block
pattern = r'(        \.container \{[^}]+\})\s*(        \.container::before \{[^}]+\})'
replacement = v4_container

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open('INDEX.HTML', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ V4 Premium upgrade applied successfully!")
