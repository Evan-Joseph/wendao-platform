# **个性化在线自学平台 - API 接口规范文档**

## 1. 概述

本 API 接口规范文档旨在定义个性化在线自学平台各模块的接口，包括请求方法、请求参数、返回值格式和错误代码。通过这些接口，前端与后端以及不同模块之间能够高效地进行数据交互。每个接口设计遵循 RESTful 风格，返回值使用 JSON 格式，所有请求均需进行身份验证。

## 2. 通用规范

- **请求协议**：HTTPS
- **身份验证**：JWT（JSON Web Token）
- **请求格式**：JSON
- **响应格式**：JSON
- **错误处理**：标准 HTTP 状态码和自定义错误信息

### 2.1 请求头
- `Content-Type`: `application/json`
- `Authorization`: `Bearer <JWT>`

### 2.2 响应结构
```json
{
  "status": "success" | "error",
  "data": { ... },
  "message": "<描述信息>"
}
```

## 3. 用户管理模块

### 3.1 用户注册
- **URL**: `/api/v1/users/register`
- **方法**: `POST`
- **描述**: 允许新用户注册并创建账号。
- **请求参数**:
  - `username` (string, 必填): 用户名，3-30 个字符。
  - `email` (string, 必填): 用户邮箱，需符合电子邮件格式。
  - `password` (string, 必填): 用户密码，最少 8 个字符。
- **响应**:
  - `status`: 注册状态。
  - `data`: 用户信息（`user_id`, `username`, `email`）。
- **错误代码**:
  - `400`: 请求参数错误，例如参数缺失或格式不正确。
  - `409`: 用户名或邮箱已存在。
  - `422`: 参数验证失败（如密码过短）。

### 3.2 用户登录
- **URL**: `/api/v1/users/login`
- **方法**: `POST`
- **描述**: 用户登录，获取 JWT。
- **请求参数**:
  - `email` (string, 必填): 用户邮箱。
  - `password` (string, 必填): 用户密码。
- **响应**:
  - `status`: 登录状态。
  - `data`: JWT (`token`), 用户信息 (`user_id`, `username`)。
- **错误代码**:
  - `400`: 请求参数错误。
  - `401`: 认证失败。
  - `429`: 登录尝试过多。

### 3.3 获取用户信息
- **URL**: `/api/v1/users/{user_id}`
- **方法**: `GET`
- **描述**: 获取用户的详细信息。
- **请求参数**: 无。
- **响应**:
  - `status`: 获取状态。
  - `data`: 用户信息 (`user_id`, `username`, `email`, `registration_date`, `learning_progress`)。
- **错误代码**:
  - `404`: 用户不存在。

## 4. 问卷生成模块

### 4.1 获取问卷
- **URL**: `/api/v1/questionnaire/{user_id}`
- **方法**: `GET`
- **描述**: 根据用户信息生成知识评估问卷。
- **请求参数**: 无。
- **响应**:
  - `status`: 获取状态。
  - `data`: 问卷 (`questionnaire_id`, `questions`)。
  - `metadata`: 生成时间和到期时间等元数据。
- **错误代码**:
  - `404`: 用户不存在。

### 4.2 提交问卷
- **URL**: `/api/v1/questionnaire/submit`
- **方法**: `POST`
- **描述**: 提交用户填写的问卷。
- **请求参数**:
  - `user_id` (string, 必填): 用户 ID。
  - `questionnaire_id` (string, 必填): 问卷 ID。
  - `answers` (array, 必填): 用户答案列表。
- **响应**:
  - `status`: 提交状态。
  - `data`: 分析结果 (`knowledge_level`, `recommended_path`)。
- **错误代码**:
  - `400`: 请求参数错误。
  - `410`: 问卷已过期。

## 5. 学习路径生成模块

### 5.1 获取学习路径
- **URL**: `/api/v1/learning-path/{user_id}`
- **方法**: `GET`
- **描述**: 获取用户的个性化学习路径。
- **请求参数**: 无。
- **响应**:
  - `status`: 获取状态。
  - `data`: 学习路径 (`path_id`, `nodes`, `relationships`)。
  - `progress`: 当前路径的学习进度。
- **错误代码**:
  - `404`: 用户不存在或路径未生成。

### 5.2 更新学习路径
- **URL**: `/api/v1/learning-path/update`
- **方法**: `PUT`
- **描述**: 根据用户反馈更新学习路径。
- **请求参数**:
  - `user_id` (string, 必填): 用户 ID。
  - `feedback` (object, 必填): 用户反馈数据。
- **响应**:
  - `status`: 更新状态。
  - `data`: 更新后的学习路径信息。
  - `suggested_changes`: 对学习路径的建议更改内容。
- **错误代码**:
  - `400`: 请求参数错误。
  - `404`: 学习路径未找到。

## 6. 学习资源管理模块

### 6.1 获取学习资源
- **URL**: `/api/v1/resources`
- **方法**: `GET`
- **描述**: 获取学习资源列表。
- **请求参数**:
  - `tags` (array, 可选): 资源标签筛选。
  - `difficulty_level` (string, 可选): 资源难度等级（如初级、中级、高级）。
  - `page` (int, 可选): 分页参数。
- **响应**:
  - `status`: 获取状态。
  - `data`: 学习资源列表 (`resource_id`, `name`, `type`, `description`, `difficulty_level`)。
  - `pagination`: 分页信息 (`current_page`, `total_pages`)。
- **错误代码**:
  - `404`: 资源不存在。

### 6.2 上传学习资源
- **URL**: `/api/v1/resources/upload`
- **方法**: `POST`
- **描述**: 上传新的学习资源。
- **请求参数**:
  - `name` (string, 必填): 资源名称。
  - `type` (string, 必填): 资源类型。
  - `description` (string, 可选): 资源描述。
  - `file` (file, 必填): 资源文件。
  - `tags` (array, 可选): 标签列表。
  - `difficulty_level` (string, 可选): 资源难度等级。
- **响应**:
  - `status`: 上传状态。
  - `data`: 资源信息 (`resource_id`, `name`)。
- **错误代码**:
  - `400`: 请求参数错误。
  - `409`: 资源已存在。
  - `413`: 文件大小超过限制。

## 7. 家教服务对接模块

### 7.1 获取家教列表
- **URL**: `/api/v1/tutors`
- **方法**: `GET`
- **描述**: 获取可用家教的列表。
- **请求参数**:
  - `subject` (string, 可选): 过滤家教的学科。
  - `location` (string, 可选): 过滤家教的地理位置。
  - `rating` (float, 可选): 家教评分筛选（如 4.5 以上）。
- **响应**:
  - `status`: 获取状态。
  - `data`: 家教列表 (`tutor_id`, `name`, `subjects`, `rating`, `availability`)。
  - `availability`: 家教的可预约时段。
- **错误代码**:
  - `404`: 无家教可用。

### 7.2 预约家教
- **URL**: `/api/v1/tutors/book`
- **方法**: `POST`
- **描述**: 预约家教服务。
- **请求参数**:
  - `user_id` (string, 必填): 用户 ID。
  - `tutor_id` (string, 必填): 家教 ID。
  - `time_slot` (string, 必填): 预约时间。
- **响应**:
  - `status`: 预约状态。
  - `data`: 预约确认信息 (`booking_id`, `tutor_name`, `time_slot`)。
- **错误代码**:
  - `400`: 请求参数错误。
  - `409`: 时间冲突。
  - `404`: 家教不可用。

## 8. 错误代码说明

- **400 Bad Request**: 请求参数有误。
- **401 Unauthorized**: 认证失败，用户无权限。
- **403 Forbidden**: 用户无权限访问该资源。
- **404 Not Found**: 请求的资源不存在。
- **409 Conflict**: 请求与当前状态冲突，例如资源已存在或时间冲突。
- **410 Gone**: 资源不再可用或已过期。
- **413 Payload Too Large**: 上传的文件大小超过限制。
- **422 Unprocessable Entity**: 请求参数验证失败。
- **429 Too Many Requests**: 请求频率过高。
- **500 Internal Server Error**: 服务器内部错误。

如果有其他需要补充或修改的内容，欢迎随时与我沟通。

