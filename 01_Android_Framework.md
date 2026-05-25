# 📁 Category 0: The Android Framework

이 파일에는 안드로이드 프레임워크 기초부터 시스템 아키텍처, 런타임, 빌드 최적화까지 책의 순서대로 요약한 내용을 누적합니다.
나중에 `Ctrl + F`로 키워드를 검색하는 나만의 지식 창고로 활용합니다.

---

## 📌 [X] Q0. What is Android?
- **내 문장 요약:**
  - 안드로이드는 Google이 개발·유지하는 리눅스 커널 기반의 오픈소스 모바일 OS로, 스마트폰·태블릿 등 다양한 하드웨어를 지원하는 유연한 플랫폼입니다.
  - Framework API 요청이 ART·HAL·Linux Kernel을 거쳐 앱 실행과 하드웨어 접근이 이뤄지는 계층형 OS입니다.
- **Deep Dive & 키워드 메모:**
  - **Key Features(책 ①→⑤):** AOSP 커스터마이즈(웨어러블·TV·IoT) → Kotlin/Java·SDK·Android Studio → Google Play·서드파티 → 멀티태스킹·GC → 다양한 화면·가격대
  - **Architecture(책 순):** Linux Kernel(메모리·프로세스·보안·드라이버) ➡️ HAL(표준 인터페이스·동적 로드) ➡️ ART(AOT·JIT)·Core Libraries ➡️ Native(OpenGL·SQLite·WebKit) ➡️ Framework(ActivityManager, NotificationManager, Content Providers) ➡️ Applications
  - **Practical Q — *How do Linux Kernel, ART, and HAL work together for application execution and hardware interaction?*:** Framework가 하드웨어 접근을 요청하면 ➡️ ART가 앱 실행 ➡️ HAL이 표준 인터페이스로 장치에 맞춤(필요 시 모듈 동적 로드) ➡️ Linux Kernel이 드라이버로 실제 하드웨어 제어
  - **💡 (책):** 오픈소스로 확산·커스터마이즈, HAL은 Framework API–하드웨어 연결, ART AOT·JIT는 실행 성능 최적화

---

## 📌 [ ] Q1. What is Intent?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q2. What is the purpose of Pending Intent?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q3. What are the differences between Serializable and Parcelable
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q4. What is Context and what types of Context exist?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q5. What is Application class?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q6. What is the purpose of the AndroidManifest file?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q7. Describe the Activity lifecycle
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q8. Describe the Fragment lifecycle
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q9. What is Service?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q10. What is BroadcastReceiver?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q11. What is the purpose of a ContentProvider, and how does it facilitate secure data sharing between applications?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q12. How to handle configuration changes?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q13. How Android handles memory management, and how do you avoid memory leaks?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q14. What are the main causes of ANR errors, and how can you prevent them from occurring?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q15. How do you handle deep links?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q16. What are tasks and back stack?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q17. What's the purpose of Bundle?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q18. How do you pass data between Activities or Fragments
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q19. What happens to an Activity during configuration changes?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q20. What is ActivityManager?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q21. What are the advantages of using SparseArray
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q22. How do you handle runtime permissions?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q23. What are the roles of Looper, Handler, and HandlerThread?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q24. How do you trace exceptions?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q25. What are build variants and flavors?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q26. How do you ensure accessibility?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q27. What is the Android file system?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q28. What are Android Runtime (ART), Dalvik, and Dex Compiler?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q29. What are the differences between the APK file and the AAB file?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q30. What is R8 optimization?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q31. How do you reduce application sizes?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  - 

---

## 📌 [ ] Q32. What is a process in Android applications, and how does the Android operating system manage it?
- **내 문장 요약:**
  - 
- **Deep Dive & 키워드 메모:**
  -