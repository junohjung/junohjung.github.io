# Junoh Jung — academic website

Academic Pages 기반의 영어 연구자 웹사이트입니다. **현재 비공개 검토용**입니다.

- GitHub 저장소: https://github.com/junohjung/junohjung.github.io (Private)
- 비공개 미리보기: https://junoh-jung-research.green-cow-6910.chatgpt.site (소유자 로그인 필요)
- GitHub Pages 공개 배포는 내려져 있습니다. 자동 배포 워크플로는 없습니다.
- `robots.txt`와 `noindex`는 검색 노출 방지용이며 접근 제어가 아닙니다. 미리보기 접근 제어는 Sites가 담당합니다.

## 내용 수정

| 내용 | 파일 |
| --- | --- |
| 이름, 소속, 프로필 사진 | `_config.yml`, `_includes/author-profile.html` |
| 첫 화면 소개 | `index.md` |
| 연구 소개 | `_pages/research.md` |
| 논문 | `_publications/*.md` |
| CV 경력 요약 | `_pages/cv.md` |
| 강의·발표 | `_pages/teaching-talks.md` |
| 메뉴 | `_data/navigation.yml` |
| 사진·연구 그림 | `images/` |
| CV PDF | `files/CV_Jung_Sep2026_public.pdf` |
| 개인 디자인 | `assets/css/junoh.css` |

각 논문 Markdown의 메타데이터에서 `status`, `year`, `doi`, `manuscript` 등을 수정합니다. `group`은 `published`, `conference`, `ongoing` 중 하나입니다. 원고 준비 중인 항목에 추정 출판 연도를 넣지 않습니다.

## 로컬 미리보기

Ruby와 Bundler 설치 후:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

일반 빌드: `bundle exec jekyll build`. 비공개 미리보기 빌드: `bundle exec jekyll build --config _config.yml,_config.preview.yml`.
출력은 `dist/`이며 Git에는 포함되지 않습니다. `.openai/hosting.json`은 비공개 Sites 미리보기 설정입니다.

## 자료와 확인 사항

- 2026년 9월 CV를 기본 자료로 사용했습니다.
- CV PDF의 전화번호와 체류 신분만 실제 PDF 콘텐츠에서 삭제했습니다. 원본 파일은 변경하지 않았습니다.
- 웹사이트의 출판 논문 네 편은 출판사 기록과 대조했고 DOI·arXiv 링크를 넣었습니다. 2025·2026년 JFM 및 2024년 TCFD 제목은 CV 표현 대신 최종 출판 제목을 사용했습니다. PDF의 논문 제목은 제공된 원본 문구를 유지합니다.
- 프로필 사진: Aaron Towne 연구실의 Junoh Jung 소개 페이지. https://atowne.com/people/
- 유동 추정 결과 그림: Jung & Towne (2026), JFM 1033, A22, Figure 16, CC BY 4.0. https://doi.org/10.1017/jfm.2026.11444
- 나머지 두 연구 방향에는 명시적으로 개념도만 넣었습니다. 실제 결과 그림이 준비되면 해당 위치에 교체할 수 있습니다.
- 템플릿: Academic Pages, MIT License. 원본 LICENSE를 보존했습니다.

## 나중에 GitHub Pages로 공개할 때

현재 비공개 요청이 유지되므로 아래 작업을 자동으로 실행하지 않습니다.

1. 웹사이트 내용과 CV를 검토한 뒤 공개 전환을 명시적으로 요청합니다.
2. `_config.yml`에서 `private_preview`를 `false`로 설정하고 `robots.txt`를 공개용으로 변경합니다.
3. 공개할 저장소와 GitHub 요금제에 맞춰 Pages를 설정합니다. **비공개 저장소라고 해서 GitHub Pages 사이트도 비공개인 것은 아닙니다.**
4. Pages의 소스를 `main` 브랜치와 루트로 설정하고 배포 후 HTTPS와 모든 페이지를 확인합니다.
5. 필요할 때 개인 도메인을 구매·연결합니다. 현재 구입하거나 연결한 도메인은 없습니다.
