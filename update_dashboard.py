import re
import os

def get_file_stats(file_name, expected_total, start_q, end_q):
    """파일을 읽어서 완료된 질문 수와 진척률을 반환합니다."""
    if not os.path.exists(file_name):
        return 0, expected_total, 0, "대기 중"
    
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
    
    pattern = r"## 📌 \s*\[([ xX]?)\]\s*Q(\d+)\."
    matches = re.findall(pattern, content)
    
    if not matches:
        return 0, expected_total, 0, "0%"
    
    valid_matches = []
    for checked, q_num_str in matches:
        q_num = int(q_num_str)
        if start_q <= q_num <= end_q:
            valid_matches.append(checked)
            
    total_q = len(valid_matches) if len(valid_matches) > 0 else expected_total
    completed_q = sum(1 for checked in valid_matches if checked.lower() == 'x')
    percent = int((completed_q / total_q) * 100) if total_q > 0 else 0
    
    status_str = f"{percent}%" if completed_q > 0 else "0%"
    return completed_q, total_q, percent, status_str

def generate_dashboard():
    sections = [
        {"id": "1구간", "topic": "Framework 기초", "file": "01_Android_Framework.md", "total": 10, "range": "Q0 ~ Q9", "start": 0, "end": 9},
        {"id": "2구간", "topic": "Framework 심화 & 시스템", "file": "01_Android_Framework.md", "total": 12, "range": "Q10 ~ Q21", "start": 10, "end": 21},
        {"id": "3구간", "topic": "스레드 & 빌드 최적화", "file": "01_Android_Framework.md", "total": 11, "range": "Q22 ~ Q32", "start": 22, "end": 32},
        {"id": "4구간", "topic": "전통 UI - Views", "file": "02_Android_Views.md", "total": 16, "range": "Q33 ~ Q48", "start": 33, "end": 48},
        {"id": "5구간", "topic": "Jetpack & Business Logic", "file": "03_Jetpack_Logic.md", "total": 18, "range": "Q49 ~ Q66", "start": 49, "end": 66},
    ]
    
    table_rows = []
    total_completed = 0
    total_questions = 0
    section_1_list_str = ""
    
    for sec in sections:
        comp, tot, pct, status = get_file_stats(sec["file"], sec["total"], sec["start"], sec["end"])
        total_completed += comp
        total_questions += tot
        
        pct_display = f"**{status}**" if comp > 0 else status
        table_rows.append(f"| **{sec['id']}** | {sec['topic']} | {sec['range']} | {comp} / {tot} | {pct_display} |")
        
        if sec["id"] == "1구간" and os.path.exists(sec["file"]):
            with open(sec["file"], "r", encoding="utf-8") as f:
                content = f.read()
            matches = re.findall(r"## 📌 \s*\[([ xX]?)\]\s*(Q\d+)\.\s*(.*)", content)
            
            list_items = []
            for checked, q_num, q_title in matches:
                if int(re.sub(r"\D", "", q_num)) <= 9:
                    status_box = "[X]" if checked.lower() == 'x' else "[ ]"
                    list_items.append(f"- {status_box} {q_num}. {q_title}")
            section_1_list_str = "\n".join(list_items)

    if not section_1_list_str:
        section_1_list_str = "- [ ] Q0. What is Android?\n- [ ] Q1. What is Intent?\n- [ ] Q2. What is the purpose of Pending Intent?"

    overall_percent = int((total_completed / total_questions) * 100) if total_questions > 0 else 0

    # 🔥 버그 방지: 중괄호 충돌을 피하기 위해 프로그래스 바 문자열을 미리 조립합니다.
    bar_length = overall_percent // 5
    space_length = 20 - bar_length
    progress_bar_str = "[" + "=" * bar_length + " " * space_length + "] " + str(overall_percent) + "%"
    table_content_str = "\n".join(table_rows)

    # 3. README.md 내용 조립
    readme_content = f"""# 🤖 Android Core Deep Dive

> 《Manifest Android Interview》를 순서대로 파고들며 안드로이드 핵심 원리를 내 언어로 정리하는 저장소입니다.
> **🤖 이 대시보드는 GitHub Actions에 의해 자동으로 업데이트됩니다.**

---

## 📊 전체 진행률 (Overall Progress)
`{total_completed} / {total_questions} 개의 질문 파괴 완료 ({overall_percent}%)`
```text
{progress_bar_str}