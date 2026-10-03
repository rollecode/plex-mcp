### 1.2.0: 2026-10-03

* Expose 25 core tools instead of 405
* Add find_operation and run_operation for the rest
* Cut tool definitions from 84 000 to 8 400 tokens

### 1.1.0: 2026-10-02

* Page results larger than 20 000 tokens
* Add get_result_page to page, filter and narrow them
* Parse JSON bodies containing invalid UTF-8

### 1.0.2: 2026-09-28

* Keep idle sessions for 24 hours

### 1.0.1: 2026-09-19

* Report its own name, not Cronometer's

### 1.0.0: 2026-09-15

* Every Plex API operation as a tool
* Routes each call to the server or to plex.tv
* Tools generated from the community OpenAPI spec
* Stable client identifier, stored once
* Coverage test compares tools against the spec