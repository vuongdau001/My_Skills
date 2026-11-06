# Nguồn tham khảo và cách điều chỉnh cho CRM

Mã tài liệu: **CRM-SOURCES** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Phân biệt nội dung nguồn gốc với quy trình nội bộ.

**Đọc khi:** Cần giải thích tại sao chọn phương pháp hoặc thay đổi chuẩn.


<a id="spec-2"></a>

## Cơ sở chuẩn và cách áp dụng

| Nguồn chính thức | Phần tham khảo | Cách sử dụng trong CRM |
|---|---|---|
| [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) | Requirements engineering và nội dung thông tin liên quan | Cơ sở tổ chức hồ sơ yêu cầu; không tuyên bố bảng Epic/Story dưới đây là template nguyên văn của ISO |
| [IREB CPRE Glossary](https://cpre.ireb.org/en/downloads-and-resources/glossary) | Completeness, consistency, verifiability và validation | Phân biệt đủ nội dung trong scope, không mâu thuẫn, kiểm chứng được và đúng nhu cầu |
| [IREB CPRE Foundation syllabus 3.3.0, mục 3.8 và 4.4](https://hub.ireb.org/media/pages/resources/cpre-foundation-level-syllabus/9c084b1cfd-1787039954/cpre_foundationlevel_syllabus_en_v.3.3.0.pdf) | Quality criteria ở hai mức và cách validation | Bổ sung quality review từng requirement và cả bộ hồ sơ, có stakeholder, góc nhìn và review lặp |
| [NASA Systems Engineering Handbook, Appendix C](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) | Checklist viết và validation requirement, nhất là C.4 | Tham khảo các câu hỏi kiểm thực tế, rồi điều chỉnh thành thủ tục review CRM |
| [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2) | Ký pháp mô hình quy trình nghiệp vụ | Dùng khi cần làm rõ trách nhiệm, sự kiện, nhánh và phối hợp nhiều bên |
| [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1) | Ký pháp mô hình, gồm hành vi/trạng thái/tương tác | Tham khảo khi dùng state machine hoặc sequence diagram; phải phân biệt diagram minh họa và mô hình đúng ký pháp |
| [ISTQB CTFL v4.0.1, mục 4.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) | Equivalence partitioning, boundary values, decision tables, state transitions | Kỹ thuật rà thiếu test condition và phản ví dụ từ mô hình; không biến số testcase thành bằng chứng spec đúng |

ISO công khai xác định phạm vi quá trình và information items của requirements engineering. Bảng chi tiết dưới đây là **chuẩn nội bộ đề xuất cho CRM**, được điều chỉnh từ các nguyên tắc/kỹ thuật tham khảo. Chưa đối chiếu toàn văn trả phí để kết luận tuân thủ điều khoản ISO, và không có một checklist Epic/Story duy nhất bắt buộc cho mọi dự án.


<a id="workflow-18"></a>

## Tài liệu tham khảo

Các nguồn giúp định nghĩa khái niệm; workflow, hierarchy Capability-trên-Epic và các checklist của CRM trong tài liệu này là đề xuất điều chỉnh cho dự án:

- [IIBA — Global Business Analysis Core Standard](https://www.iiba.org/globalassets/standards-and-resources/core-standard/iiba-core-standard.pdf): phân loại và quản lý requirement.
- [Scrum Guide 2020 — Definition of Done](https://scrumguides.org/scrum-guide.html#commitment-definition-of-done): DoD gắn với chất lượng Increment.
- [Scrum Alliance — Definition of Ready vs. Definition of Done](https://resources.scrumalliance.org/Article/definition-vs-ready): phân biệt điều kiện bắt đầu và hoàn thành.
- [Scrum Alliance — Agile Glossary](https://www.scrumalliance.org/glossary/): Acceptance Criteria.
- [Scrum Guide — Product Backlog và refinement](https://scrumguides.org/scrum-guide.html#product-backlog): refinement là hoạt động làm rõ backlog; cách phân rã công việc được điều chỉnh theo nhu cầu của đội. Việc không tạo Task phân tích mặc định trong tài liệu này là quyết định tổ chức đề xuất cho CRM.
- [Microsoft — Define features and epics](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops): ví dụ hierarchy Epic → Feature của Azure Boards, để phân biệt với quy ước CRM.
- [Atlassian — Configure the work type hierarchy](https://support.atlassian.com/jira-cloud-administration/docs/configure-the-issue-type-hierarchy): các mức work item và giới hạn cấu hình.
- [Atlassian — Best practices on the Resolution field](https://support.atlassian.com/jira/kb/best-practices-on-using-the-resolution-field-in-jira-cloud/): ảnh hưởng của Resolution đối với trạng thái “resolved” trong hệ thống.


## Nguồn cho cách chia backlog và giới hạn áp dụng

| Nguồn | Học gì | CRM điều chỉnh gì |
|---|---|---|
| [Azure Boards — Define features and epics](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops) | Agile process có Epic → Feature → User Story → Task | CRM đặt Capability trên Epic trong tài liệu; không gọi đó là nguyên mẫu Azure |
| [Jira — work types](https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-types/) | Mặc định Epic → Story/Task/Bug → Subtask | Dùng Task thuộc Epic và link tới Story khi không có parent-child phù hợp; chưa xác minh tenant |
| [Scrum Guide](https://scrumguides.org/scrum-guide.html) | Refinement làm rõ dần; Developers tổ chức kế hoạch thực hiện | Không bắt ticket Task; dùng DoR/checklist theo bối cảnh CRM |
| [Agile Alliance — Story Splitting](https://agilealliance.org/glossary/story-splitting/) | Story nhỏ hơn vẫn có giá trị nghiệp vụ đo được | Tách theo hành vi; không chia Story mặc định theo frontend/backend/test |
| [Bill Wake — INVEST and SMART Tasks](https://xp123.com/invest-in-good-stories-and-smart-tasks/) | INVEST chất lượng Story; SMART chất lượng Task | Catalog T01–T08 là cách CRM áp dụng SMART, không phải nguyên văn nguồn |
| [Cucumber — Example Mapping](https://cucumber.io/blog/bdd/example-mapping-introduction/) | Thảo luận rules/examples/questions để hiểu chung | Dùng trong refinement Story và phần hành vi của Epic cần làm rõ; không thay toàn bộ mô hình Epic |

Các bảng E/S/T, Q01–Q07, gate, mẫu số inventory và cách đặt Capability là chuẩn nội bộ đề xuất đã được chọn để đóng gói. ISO/IREB/NASA cung cấp nền tảng chất lượng yêu cầu; OMG ký pháp mô hình; ISTQB kỹ thuật review/test. Không nguồn nào được dẫn ở đây ban hành nguyên bộ checklist CRM. Không tuyên bố đạt mức CMMI hoặc tuân thủ toàn văn ISO từ việc dùng gói này.

Duy trì citation gần nội dung sử dụng. Khi thay đổi tiêu chí, ghi rõ là từ nguồn, diễn giải hay quyết định CRM; xác minh lại tài liệu gốc nếu phiên bản hoặc cách dùng có thay đổi. Ngày đối chiếu cho lần đóng gói này: 02/11/2026; không sao chép toàn văn tiêu chuẩn trả phí.


## Bổ sung vận hành 1.3 — 03/11/2026

C01–C08, mapping E/S→model/evidence, policy register, quy ước ID và cách đo/roll-up là **CRM tailoring** để làm rõ cách sử dụng các nguyên tắc đã dẫn, không phải danh mục/công thức nguyên bản của IREB, Scrum hay CMMI. Bản 1.3 không cập nhật phiên bản nguồn tham khảo hoặc tuyên bố đã khảo sát lại toàn bộ nguồn ngoài. Không thêm framework mới chỉ để đặt tên cho checklist.

Business/Stakeholder requirements tiếp tục dùng Q01–Q07; phương pháp kiểm chứng theo cấp độ và context. Loại requirement và cấp backlog là hai chiều; ID có type metadata riêng. Phân biệt acceptance sản phẩm với business benefits observation, chưa có dữ liệu thì không tuyên bố lợi ích đạt. Policy và các ngưỡng dự án phải được authority xác nhận, không được suy từ ví dụ.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
