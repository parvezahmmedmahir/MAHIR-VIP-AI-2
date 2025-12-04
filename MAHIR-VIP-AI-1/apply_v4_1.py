import re

# Read HTML
with open('INDEX.HTML', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Enhanced background colors - Gold, Purple, Pink
content = re.sub(
    r'radial-gradient\(circle at 20% 50%, rgba\(8, 8, 8, 0\.1\)',
    'radial-gradient(circle at 20% 50%, rgba(255, 215, 0, 0.12)',
    content
)
content = re.sub(
    r'radial-gradient\(circle at 80% 80%, rgba\(17, 17, 17, 0\.1\)',
    'radial-gradient(circle at 80% 80%, rgba(138, 43, 226, 0.1)',
    content
)
content = re.sub(
    r'radial-gradient\(circle at 40% 20%, rgba\(12, 12, 12, 0\.08\)',
    'radial-gradient(circle at 40% 20%, rgba(255, 105, 180, 0.08)',
    content
)

# 2. Premium Generate Button - Gold gradient
generate_btn_old = r'\.generate-btn \{[^}]+background: linear-gradient\(45deg, var\(--primary\), var\(--secondary\)\);[^}]+\}'
generate_btn_new = '''.generate-btn {
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%);
            color: #000;
            border: none;
            padding: 20px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 16px;
            cursor: pointer;
            width: 100%;
            margin: 20px 0;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 
                0 4px 15px rgba(255, 215, 0, 0.4),
                0 0 0 1px rgba(255, 215, 0, 0.2) inset,
                0 8px 25px rgba(255, 140, 0, 0.3);
            position: relative;
            overflow: hidden;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
        }'''
content = re.sub(generate_btn_old, generate_btn_new, content, flags=re.DOTALL)

# 3. Generate Button Hover
content = re.sub(
    r'\.generate-btn:hover \{[^}]+\}',
    '''.generate-btn:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 
                0 6px 20px rgba(255, 215, 0, 0.6),
                0 0 0 1px rgba(255, 215, 0, 0.4) inset,
                0 12px 35px rgba(255, 140, 0, 0.5);
            background: linear-gradient(135deg, #FFE55C 0%, #FFB347 50%, #FF9500 100%);
        }''',
    content,
    flags=re.DOTALL
)

# 4. Premium Join Button - Purple gradient
join_btn_old = r'\.join-btn \{[^}]+background: linear-gradient\(45deg, var\(--secondary\), #8a2be2\);[^}]+\}'
join_btn_new = '''.join-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #8a2be2 100%);
            color: white;
            border: none;
            padding: 16px;
            font-size: 17px;
            font-weight: 600;
            border-radius: 14px;
            cursor: pointer;
            width: 100%;
            margin: 15px 0;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 
                0 4px 15px rgba(102, 126, 234, 0.4),
                0 0 0 1px rgba(138, 43, 226, 0.2) inset,
                0 8px 25px rgba(118, 75, 162, 0.3);
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }'''
content = re.sub(join_btn_old, join_btn_new, content, flags=re.DOTALL)

# 5. Join Button Hover
content = re.sub(
    r'\.join-btn:hover \{[^}]+transform: translateY\(-3px\);[^}]+\}',
    '''.join-btn:hover {
            transform: translateY(-3px) scale(1.01);
            box-shadow: 
                0 6px 20px rgba(102, 126, 234, 0.6),
                0 0 0 1px rgba(138, 43, 226, 0.4) inset,
                0 12px 35px rgba(118, 75, 162, 0.5);
            background: linear-gradient(135deg, #7c94f5 0%, #8b5fb8 50%, #9d4edd 100%);
        }''',
    content,
    flags=re.DOTALL
)

# Write back
with open('INDEX.HTML', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ V4.1 Premium buttons and background applied!")
print("🎨 Background: Gold, Purple, Pink gradients")
print("🔘 Buttons: Enhanced with premium gradients and glow effects")
