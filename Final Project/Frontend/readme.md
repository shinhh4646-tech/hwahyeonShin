
1. 홈 & 알림 (Home & Alerts)

1-1.home.html: 친구들의 최신 게시물을 스크롤하며 확인할 수 있는 메인 피드 화면

1-2.alert.html: 부적절한 사용자나 스팸 게시물을 신고하는 화면

2. 탐색 & 검색 (Explore & Search)

2-1.explore.html: 새로운 '피드를 발견하고 실시간으로 유저를 검색하는 탐색 탭


3. 작성 (Create)

3-1.create_post.html: 카메라로 사진을 찍고 캡션을 달아 그래프에 새 게시물을 추가하는 화면


4. 내 프로필 (My Profile)

4-1.my_profile.html: 내 게시물 수, 팔로워 통계 및 수집한 화면

4-2.connections.html: 내 인맥 그래프(팔로워/팔로잉) 리스트를 시각적으로 보여주는 화면

4-3.feed.html: 내 프로필 그리드에서 선택한 게시물들을 크게 피드 형태로 모아보는 상세 뷰 화면

5. 인증 & 인터랙션 (Auth & Interaction)

5-1.login.html: 사용자가 앱에 로그인하는 화면

5-2.signup.html: 새로운 유저가 자신의 정보를 등록하여 네트워크에 참여하는 가입 화면입

5-3.likes.html: 특정 게시물에 공감(좋아요 edge)을 표시한 유저들의 명단입니다.

6. 친구 프로필 (Friend's Profile)

6-1.friends_profile.html: 다른 유저의 프로필을 탐색하는 화면

6-2.friends_connections.html: 친구가 맺고 있는 인맥 리스트 화면

6-3.friends_feed.html: 친구의 프로필 그리드에서 넘어와 해당 친구의 게시물만 피드로 보는 화면









root {
            --bg-color: #000000;
            --text-main: #FFFFFF;
            --text-sub: #A8A8A8;
            --border-color: #262626;
            --button-bg: #1A1A1A;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding-bottom: 60px;
        }



    <nav>
        <a href="1-1.home.html" class="nav-item">🏠</a>
        <a href="2-1.explore.html" class="nav-item active">🔍</a>
        <a href="3-1.create_post.html" class="nav-item">📸</a>
        <a href="4-1.my_profile.html" class="nav-item">👤</a>
    </nav>
