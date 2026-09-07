#!/usr/bin/env python3
"""将 travel-guides.yaml 转换为 HTML 卡片集成到 index.html"""

import yaml
import re
from pathlib import Path


def load_yaml(yaml_path):
    """加载YAML配置"""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def format_stats(stats):
    """格式化热度信息"""
    if not stats:
        return ""
    likes = stats.get('likes', 0)
    collects = stats.get('collects', 0)
    
    if likes is None or collects is None:
        return ""
    
    # 格式化数字
    def format_num(n):
        if n >= 10000:
            return f"{n/10000:.1f}万"
        elif n >= 1000:
            return f"{n/1000:.1f}千"
        return str(n)
    
    return f"👍{format_num(likes)} ⭐{format_num(collects)}"


def generate_daily_cards(guides, day):
    """生成每日攻略卡片HTML（紧凑版）"""
    day_guides = [g for g in guides if g.get('day') == day]
    if not day_guides:
        return ""
    
    # 按地点分组
    guides_by_location = {}
    for g in day_guides:
        loc = g.get('location', '其他')
        if loc not in guides_by_location:
            guides_by_location[loc] = []
        guides_by_location[loc].append(g)
    
    html = '<div class="guide-section-daily">\n'
    html += '  <div class="guide-toggle" onclick="this.parentElement.classList.toggle(\'expanded\')">📖 攻略推荐 ▼</div>\n'
    html += '  <div class="guide-collapsed">\n'
    
    # 根据攻略数量自适应显示
    total_guides = len(day_guides)
    
    if total_guides <= 3:
        # 少量攻略：全部显示
        for g in day_guides:
            html += generate_mini_card(g)
    else:
        # 多量攻略：按地点分组显示
        for loc, loc_guides in guides_by_location.items():
            html += f'    <div class="guide-location-group">\n'
            html += f'      <div class="guide-location-title">📍 {loc}</div>\n'
            for g in loc_guides[:2]:  # 每个地点最多显示2条
                html += generate_mini_card(g)
            if len(loc_guides) > 2:
                html += f'      <div class="guide-more">+{len(loc_guides) - 2} 更多</div>\n'
            html += f'    </div>\n'
    
    html += '  </div>\n'
    html += '</div>\n'
    return html


def generate_mini_card(guide):
    """生成迷你卡片HTML"""
    stats_str = format_stats(guide.get('stats'))
    guide_type = guide.get('type', '攻略')
    type_icon = {'美食': '🍜', '景点': '📍', '交通': '🚗', '攻略': '📖'}.get(guide_type, '📖')
    
    url = guide.get('url', '#')
    short_url = guide.get('short_url', url)
    
    # 优先使用短链接（手机友好）
    link_url = short_url if short_url else url
    
    return f'''    <a href="{link_url}" class="guide-mini-card" target="_blank">
      <span class="guide-type">{type_icon}</span>
      <span class="guide-title">{guide['title']}</span>
      <span class="guide-stats">{stats_str}</span>
    </a>\n'''


def generate_summary_cards(guides):
    """生成攻略汇总卡片HTML（详细版）"""
    # 按天分组
    guides_by_day = {}
    for g in guides:
        day = g.get('day', 0)
        if day not in guides_by_day:
            guides_by_day[day] = []
        guides_by_day[day].append(g)
    
    html = '<div class="guide-summary-container">\n'
    
    # 按天显示
    for day in sorted(guides_by_day.keys()):
        day_guides = guides_by_day[day]
        
        if day == 0:
            html += '  <div class="guide-day-section">\n'
            html += '    <h4 class="guide-day-title">📖 通用攻略</h4>\n'
        else:
            html += '  <div class="guide-day-section">\n'
            html += f'    <h4 class="guide-day-title">Day {day}</h4>\n'
        
        # 按地点分组
        guides_by_location = {}
        for g in day_guides:
            loc = g.get('location', '其他')
            if loc not in guides_by_location:
                guides_by_location[loc] = []
            guides_by_location[loc].append(g)
        
        for loc, loc_guides in guides_by_location.items():
            html += f'    <div class="guide-location-section">\n'
            html += f'      <h5 class="guide-location-name">📍 {loc}</h5>\n'
            html += f'      <div class="guide-cards-grid">\n'
            
            for g in loc_guides:
                html += generate_detail_card(g)
            
            html += f'      </div>\n'
            html += f'    </div>\n'
        
        html += '  </div>\n'
    
    html += '</div>\n'
    return html


def generate_detail_card(guide):
    """生成详细卡片HTML"""
    stats = guide.get('stats', {})
    stats_str = format_stats(stats)
    url = guide.get('url', '#')
    short_url = guide.get('short_url', url)
    
    # 美食详情
    foods_html = ""
    if 'foods' in guide:
        foods_html = '<div class="guide-foods">\n'
        for f in guide['foods']:
            foods_html += f'''      <div class="guide-food-item">
        <span class="food-name">{f['name']}</span>
        <span class="food-desc">{f.get('desc', '')}</span>
        <span class="food-location">📍{f.get('location', '')}</span>
        <span class="food-price">💰{f.get('price', '')}</span>
      </div>\n'''
        foods_html += '    </div>\n'
    
    # 景点亮点
    highlights_html = ""
    if 'highlights' in guide:
        highlights_html = '<div class="guide-highlights">\n'
        for h in guide['highlights']:
            highlights_html += f'      <div class="highlight-item">• {h}</div>\n'
        highlights_html += '    </div>\n'
    
    # 链接区域
    links_html = '<div class="guide-links">\n'
    links_html += f'      <a href="{url}" target="_blank" class="guide-link pc-link">📕 PC查看</a>\n'
    if short_url:
        links_html += f'      <a href="{short_url}" target="_blank" class="guide-link mobile-link">📱 手机打开</a>\n'
    links_html += '    </div>\n'
    
    return f'''        <div class="guide-detail-card">
          <div class="guide-header">
            <div class="guide-title-link">{guide['title']}</div>
            <span class="guide-stats">{stats_str}</span>
          </div>
          <div class="guide-summary">{guide.get('summary', '')}</div>
          {foods_html}
          {highlights_html}
          <div class="guide-tips">💡 {guide.get('tips', '')}</div>
          <div class="guide-tags">{''.join(f'<span class="tag">#{t}</span>' for t in guide.get('tags', []))}</div>
          {links_html}
        </div>\n'''


def update_index_html(index_path, daily_cards_html, summary_cards_html):
    """更新index.html中的攻略区域"""
    content = index_path.read_text(encoding='utf-8')
    
    # 更新每日攻略区域（在每个day-body中插入）
    # 这里我们先更新攻略汇总区域
    
    # 更新攻略汇总区域
    summary_pattern = r'<!-- SUMMARY_GUIDES_START -->.*?<!-- SUMMARY_GUIDES_END -->'
    summary_replacement = f'<!-- SUMMARY_GUIDES_START -->\n{summary_cards_html}<!-- SUMMARY_GUIDES_END -->'
    
    if re.search(summary_pattern, content, re.DOTALL):
        content = re.sub(summary_pattern, summary_replacement, content, flags=re.DOTALL)
    else:
        # 如果没有占位符，在小红书攻略section中插入
        content = content.replace(
            '<!-- SUMMARY_GUIDES_START -->',
            f'<!-- SUMMARY_GUIDES_START -->\n{summary_cards_html}'
        )
    
    index_path.write_text(content, encoding='utf-8')


def main():
    """主函数"""
    base = Path(__file__).parent.parent
    yaml_path = base / 'travel-guides.yaml'
    index_path = base / 'index.html'
    
    if not yaml_path.exists():
        print(f"[ERROR] YAML文件不存在: {yaml_path}")
        return
    
    if not index_path.exists():
        print(f"[ERROR] index.html不存在: {index_path}")
        return
    
    print(f"[INFO] 读取YAML: {yaml_path}")
    data = load_yaml(yaml_path)
    guides = data.get('guides', [])
    print(f"   找到 {len(guides)} 条攻略")
    
    # 生成每日攻略卡片
    print("[INFO] 生成每日攻略卡片...")
    daily_cards = ""
    for day in range(1, 6):
        day_cards = generate_daily_cards(guides, day)
        if day_cards:
            daily_cards += f"<!-- Day {day} -->\n{day_cards}\n"
    
    # 生成攻略汇总卡片
    print("[INFO] 生成攻略汇总卡片...")
    summary_cards = generate_summary_cards(guides)
    
    # 更新HTML
    print("[INFO] 更新index.html...")
    update_index_html(index_path, daily_cards, summary_cards)
    
    print("[SUCCESS] 攻略已更新到 index.html")
    print(f"   - 每日攻略卡片: {len([g for g in guides if g.get('day', 0) > 0])} 条")
    print(f"   - 通用攻略: {len([g for g in guides if g.get('day', 0) == 0])} 条")


if __name__ == '__main__':
    main()
