import streamlit as st
# st.set_page_config: 앱 전체에 영향을 주는 설정 함수 
# st.write는 다양한 객체(데이터프레임, 숫자, 리스트 등)의 “자동” 시각화에 강점
# st.markdown은 텍스트/설명/링크 등 풍부한 서식, 강조, 하이라이트에 특화 
st.set_page_config(  
    page_title='TO-DO LIST',# 브라우저의 제목
    page_icon ='🔔',# 브라우저의 아이콘 
    layout='centered' # 화면 레이아웃: 중앙 정렬    
)

# HTML: 웹페이지의 구조와 내용을 정의하는 표준 언어 
# help = : 해당 항목에 대한 도움말 
# anchor = : **HTML 앵커(id)**처럼 식별자를 부여
# ,unsafe_allow_html=True: 마크다운 문자열 안에 HTML을 직접 작성해도 렌더링해서 동작하게 만듦 
# <span style>: 짧은(인라인) 텍스트”의 일부만 스타일을 다르게 적용할 때 사용
st.markdown("# 📝나의 <span style='color:red;'>할일</span> 목록"
        #  ,anchor='title-section' # HTML 앵커:내부 링크로 이동 
        #  ,help= 'anchor 존재'
         ,unsafe_allow_html=True) 
# st.markdown: 제목과 링크를 동시에 걸 수 있음 
# st.markdown('#[텍스트 제목&링크 이름](url))
# st.markdown("# [📝나의 할일 목록](https://www.google.com)")
# st.write(): 입력한 객체를 가장 적절한 형태로 출력하는 출력함수 
st.markdown('🎯간단하고 효율적인 할일 관리를 시작해보세요!')

# divider = True : 줄 생김(구분선) 
st.header('📚사용법') # st.header: 중간 크기 제목(헤더) 
# st.subheader('🗂️할일 추가'
#              ,anchor='subheader-section1' 
#              ,help= 'subheader 존재1')
# st.subheader('🗂️완료 표시')
# st.subheader('🗂️할일 삭제')
# st.subheader('🗂️일괄 관리'
#              ,anchor='subheader-section2' 
#              ,help= 'subheader 존재2')
# st.header('📚사용법1',divider='red') #  st.markdown('## 📚사용법')
# st.header('📚사용법2',divider='orange')
# st.write('**1.할일 추가**:텍스트 입력 후 \'추가하기\' 버튼 클릭')
# st.write('**2.완료 표시**:체크박스를 클릭하여 완료 표시')
# st.write('**3.할일 삭제**:✂️버튼으로 개별 삭제')
# st.write('**4.일괄 관리**:완료된 할일만 삭제하거나 전체 삭제')

st.markdown('''
**1.할일 추가**:텍스트 입력 후 \'추가하기\' 버튼 클릭\n
**2.완료 표시**:체크박스를 클릭하여 완료 표시\n
**3.할일 삭제**:✂️버튼으로 개별 삭제\n 
**4.일괄 관리**:완료된 할일만 삭제하거나 전체 삭제
''')

# caption: 파일명/설명/사진 밑에 들어가는 "부가설명" 느낌 
# st.caption('안녕하세요.',help='캡션입니다.')
# <font size=16>환영합니다.</font>: 열었으면 닫아줘야 함 
# st.caption('안녕하세요. <font size=16>환영합니다.</font>'
#            ,unsafe_allow_html=True, # html코드처럼 보여줌? 
#            help='캡션입니다.')
# # markdown에서도 HTML 적용 가능 
# st.markdown('안녕하세요. <font size=16>환영합니다.</font>'
#            ,unsafe_allow_html=True, # html작성 허락 
#            help='캡션입니다.')

# st.code('<font size=16>환영합니다.</font>',language='html')
# line_numbers = True # 
# st.code('''a = st.button('안녕') 
# if a: # '안녕'이라는 버튼을 클릭하면 
#     st.text('버튼클릭')
# else:
#     st.text('버튼클릭 안 함 ') ''',height=150
#     ,line_numbers = True
#     ,wrap_lines=True) # wrap_lines=True: 긴 줄은 자동 줄바꿈 

# st.echo: 실행과 결과까지 출력 
# with st.echo():
#     st.write('''a = st.button('안녕') 
#              if a:
#                  st.text('버튼클릭')
#              else:
#                  st.text('버튼클릭 안 함 ')''' )
    
# def get_user_name():
#     return 'DUHO'

# with st.echo():
#     def get_p():
#         return '!!!'
    
#     g = '안녕, '
#     v = get_user_name()
#     p = get_p()

#     st.write(g,v,p)

# st.write('잘가')

# r'수식': 수학 기호 표현식  
# st.latex(r'ax^2 + bx + c = 0',help='2차 방정식')
# st.text('안녕하세요.',help='텍스트입니다.')
# df = pd.DataFrame(np.random.randn(200,3),columns=['a','b','c'])
# st.help(df)
# st.html('<font size=16>환영합니다.</font>') # 폰트 꾸미기 & 스타일 꾸미기 


def custom_warning(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem; # 내부여백
        margin: 1rem 0; # 바깥 여백
        border-left: 4px solid #ff6b35; # 왼쪽 굵은 경계선
        background-color: var(--warning-bg, #fff3cd); # 경고 배경색 
        border-radius: 0.25rem; # 박스 모서리 약간 둥글게 
        color: var(--warning-text, #856404); # 글씨색 
        font-size: 14px; # 글씨 크기
        line-height: 1.5; # 줄간격
    ">
         {message} 
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{ # 브라우저가 다크모드일 때 
            :root {{
                --warning-bg: #3d2914;
                --warning-text: #ffcc02;
            }}
        }}
        [data-theme="dark"] {{ # streamlit 테마 
            --warning-bg: #3d2914; # 경고 배경 
            --warning-text: #ffcc02; # 경고 텍스트 
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_success(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #28a745;
        background-color: var(--success-bg, #d4edda);
        border-radius: 0.25rem;
        color: var(--success-text, #155724);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --success-bg: #1e3a24;
                --success-text: #4caf50;
            }}
        }}
        [data-theme="dark"] {{
            --success-bg: #1e3a24;
            --success-text: #4caf50;
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_info(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #17a2b8;
        background-color: var(--info-bg, #d1ecf1);
        border-radius: 0.25rem;
        color: var(--info-text, #0c5460);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --info-bg: #0d2a3a;
                --info-text: #5bc0de;
            }}
        }}
        [data-theme="dark"] {{
            --info-bg: #0d2a3a;
            --info-text: #5bc0de;
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_error(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #dc3545;
        background-color: var(--error-bg, #f8d7da);
        border-radius: 0.25rem;
        color: var(--error-text, #721c24);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --error-bg: #3a1a1d;
                --error-text: #f44336;
            }}
        }}
        [data-theme="dark"] {{
            --error-bg: #3a1a1d;
            --error-text: #f44336;
        }}
    </style>
    """, unsafe_allow_html=True)

# 실전 사용 예시 
# custom_warning("이것은 경고입니다!")
# custom_success("성공적으로 완료되었습니다!")
# custom_info("참고할 만한 정보입니다.")
# custom_error("문제가 발생했습니다!")
# custom_error('에러입니다.')
# st.error('에러입니다.')

# 사용자가 할일을 입력하는 영역 명확히 구분 
st.subheader('➕새로운 할일 추가',divider='blue')

# st.text_input(): '텍스트 입력창' 
new_todo = st.text_input('할일을 입력하세요 :'
                         ,placeholder='예: 장보기,운동하기,책 읽기')
# 사용자가 텍스트를 입력한 뒤 클릭하면 submitted에 True 할당 
submitted = st.button('추가하기') 

# 여러 번 실행돼도 데이터가 사라지지 않게 "세션별 상태"로 변수 저장 
# st.session_state: 데이터를 기억하는 저장소 + 세션에 독립적으로 유지
if 'todos' not in st.session_state:
    st.session_state['todos'] = []

if submitted:
    # 입력값에서 앞 뒤 공백 제거 + 빈문자열인지 체크 
    if new_todo.strip(): # 빈문자열 여부를 판단하는 함수 
        st.session_state['todos'].append({
            # 딕셔너리: key-value  
            'task':new_todo.strip(),
            'completed': False 
        })
        custom_success(f"✅'{new_todo} 추가 완료.")
    else:
        custom_warning('💢 할일을 입력해주세요.')
st.divider()

st.subheader('📄할일 목록',divider='blue')
# st.write(st.session_state.todos)
# 할일 리스트에 할일이 하나라도 있을 때 실행 
if st.session_state['todos']:
    # 역순: reversed(range(len(st.session_state['todos'])))
    for i in reversed(range(len(st.session_state['todos']))):
        todo=st.session_state['todos'][i]

        # col1: 체크박스 자리/ col2: 할일 텍스트 자리/ col3: 
        col1,col2,col3 = st.columns([0.1,0.7,0.2])
        with col1:
            ## st.checkbox(""): 첫번째 인자는 체크박스 옆 레이블 
            completed = st.checkbox("",
            value=todo['completed'],
            key=f"check_{i}",
            help='완료 체크')

            if completed !=todo['completed']:
                st.session_state.todos[i]['completed'] = completed
                st.rerun()
        with col2:
            if completed:
                st.markdown(f"~~{todo['task']}~~",help='완료된 할일')
            else:
                st.write(todo['task'])
        # 휴지통 만들기
        with col3:
            # delete_{i}의 버튼을 누르면 pop(i) 
            if st.button('🗑️',key=f"delete_{i}",help = '삭제버튼'):
                st.session_state['todos'].pop(i) # i번째 인덱스 값을 삭제 
                custom_success('삭제되었습니다')
                # st.rerun(): 재실행 
                st.rerun()

        if i>=0:
            st.markdown('---')        
else: 
    custom_info("‼️아직 할일이 없습니다. 새로운 할일을 추가해보세요!")

if st.session_state['todos']:
    total_todos = len(st.session_state['todos'])
    completed_todos = 0
    for i in st.session_state['todos']:
        # 'completed'값이 True면 completed_todos증가 
        if i['completed']:
            completed_todos += 1
    remaining_todos = total_todos - completed_todos
    if total_todos > 0:
        completion_rate = (completed_todos/total_todos*100)
        if completion_rate == 100:
            custom_success("모든 할일 완료 🎉")
        elif completion_rate >= 80:
            custom_info("거의 완료")
        elif completion_rate >= 50:
            custom_warning("절반 완료")
        elif completion_rate == 0:
            custom_error("파이팅!")
        custom_warning(f"진행률: {completion_rate:.1f}%")
    else: 
        st.write("할 일이 없습니다. 새로운 할 일을 추가하세요.")        
    
    # Streamlit의 columns()함수로 화면을 2분할 
    # 화면이 좌우 2개 영역으로 나뉨
    # 각각의 컬럼 안에 버튼이나 원하는 UI를 배치할 수 있음 
    # 각 컬럼 안 코드는 with col1: & with col2 블록 안에서 작성 
    col1,col2 = st.columns(2)

    with col1:
        if st.button("🗑️모든 할일 삭제",type = "secondary"):
            st.session_state['todos'] = []
            custom_success("모든 할일이 삭제되었습니다.")
            st.rerun()
    with col2:
        if completed_todos > 0:
            if st.button(f"✅완료된 할일 {completed_todos}개 삭제",type = "secondary"):
                todo_list = []
                for i in st.session_state['todos']:
                    # st.session_state['todos'] = [
                    #      i for i in st.session_state['todos'] if not i['completed']
                    #        ]
                    # not completed: False 
                    if not i['completed']:
                        todo_list.append(i) 
                st.session_state['todos'] = todo_list
                custom_success("완료된 할일 {completed_todos}개가 삭제되었습니다.")
                st.rerun()

    st.subheader("📊통계")

    # title: 제목 / value: 표시할 값 / delta: 변화량 / value_color: 값의 색상 지정 
    def display_stat(title,value,delta=None,value_color=None):
        delta_str = "" # 남은 목록을 처리할 때 이용하는 것 
        if delta is not None:
            if delta >0:
                delta_str = f"(⬆️{delta})"
            elif delta <0:
                delta_str = f"(⬇️{delta})"
            else:
                delta_str = ""
        if value_color is None:
            value_color = "var(--text-color, #262730)"
        st.markdown(f"""
            <div style="
                padding: 1rem; 
                background-color: var(--stat-bg, #f0f2f6); 
                border: 1px solid var(--stat-border, transparent);
                border-radius: 10px; 
                text-align: center;
                box-shadow: var(--stat-shadow, 0 1px 3px rgba(0,0,0,0.1));
            ">
                <div style="
                    font-size: 18px; 
                    font-weight: bold; 
                    color: var(--title-color, #262730);
                    margin-bottom: 0.5rem;
                ">{title}</div>
                <div style="
                    font-size: 32px; 
                    font-weight: bold; 
                    color: {value_color};
                ">{value}{delta_str}</div>
            </div>
            <style>
                /* 라이트모드 기본값 */
                :root {{
                    --stat-bg: #f0f2f6;
                    --stat-border: transparent;
                    --stat-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    --title-color: #262730;
                    --text-color: #262730;
                }}
                
                /* 다크모드 스타일 */
                @media (prefers-color-scheme: dark) {{
                    :root {{
                        --stat-bg: #2b2b35;
                        --stat-border: #404040;
                        --stat-shadow: 0 1px 3px rgba(0,0,0,0.3);
                        --title-color: #fafafa;
                        --text-color: #fafafa;
                    }}
                }}
                
                /* Streamlit 다크모드 */
                [data-theme="dark"] {{
                    --stat-bg: #2b2b35;
                    --stat-border: #404040;
                    --stat-shadow: 0 1px 3px rgba(0,0,0,0.3);
                    --title-color: #fafafa;
                    --text-color: #fafafa;
                }}
            </style>
        """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)

    with col1:
        display_stat("전체 할일", total_todos)
    with col2:
        display_stat("완료된 할일",completed_todos,
                     delta = completed_todos,
                     value_color="#4CAF50")
    with col3:
        display_stat("남은 할일",remaining_todos,
                     delta= remaining_todos,
                     value_color="#f44336")
    
        
# 진행률 



st.divider()

st.markdown("""

""")

st.markdown("""
<style>
.footer {
    width: 90%;
    background: linear-gradient(90deg, #6dd5ed, #2193b0);
    margin-left: auto;  
    margin-right: auto;
    color: #f5f5f7;
    text-align: center;
    padding: 20px 0 16px 0;
    font-size: 1rem;
    font-weight: 400;
    box-shadow: 0 -2px 24px 0 rgba(20,20,20,0,15);
    border-radius: 32px;
    z-index: 9999;
    letter-spacing: 0.02em;
}
.footer a {
    color: #ffd600;
    font-weight: 600;
    text-decoration: none;
    margin-left: 8px;
}
.footer .icon {
    margin-right: 8px;
    font-size: 1.2em;
    vertical-align: middle;
}
</style>

<div class="footer">
    <span class="icon">📝</span>
    <span>© 2025 <b>두봉의 할일 앱</b></span>
    &nbsp;|&nbsp;
    <a href="mailto:dubong@example.com">Contact</a>
</div>
""", unsafe_allow_html=True)

# 휴지통 만들기 



















