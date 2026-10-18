import platform
print("스터디 출석부 — 실행 위치:", platform.system())
names = ["김창원", "이마산"]
for n in names:
    print(n, "출석")
    print("출석 인원:", len(names), "명")