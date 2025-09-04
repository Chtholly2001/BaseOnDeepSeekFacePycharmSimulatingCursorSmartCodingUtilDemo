#### 项目背景

当大语言模型出来时，我就在想，大语言模型面向垂直应用端会怎样节省程序员劳动。然后，我看到市面上出现了 **Cursor** 这样的编程智能体。于是我就想：能不能自己也做一个智能编程软件？

#### 基本思路

软件开发的步骤：

1. 建立项目结构
2. 编写目标文件

学习软件开发的步骤：

1. 学习一种新的框架结构
2. 将新结构复制、粘贴或迁移应用

#### 智能体设计

在编程智能体的创作中，我模仿以上思路，建立了如下步骤：

1. 智能体脚本根据用户提示词，通过大语言模型生成项目结构
2. 再生成相应的目标代码并运行

目前项目只能生成单个文件，即只完成了第二步：
智能体脚本接管编译器，通过大语言模型将用户需求转化为目标代码并运行。

#### 未来规划

未来我会继续优化，提升全栈能力，学习主流编程智能体项目，并更新如下功能：

* 加入上下文工程，实现项目结构的理解能力
* 模仿 IDEA 内嵌工具通义灵码的 DEBUG 功能
* 通过反向神经网络优化错误需求
* 模仿人类学习过程，让大语言模型对新架构进行元学习和预训练
* 探索更多大模型智能体应用

#### 技术实现

* 基于 **DeepSeek**，面向 **PyCharm** 和 **Python**，类似 **Cursor**
* 仅需在控制台提供需求，即可一键自动生成目标程序
* 原理：AI 代码生成 → 脚本写入目标文件 → 自动运行并输出结果

#### 使用价值

* 对编程小白友好
* 为专业程序员节省大量轻量级重复劳动
* 可基于简易生成的代码进行修改或提交给高级 AI 进行二次开发

#### 下一步目标

* 提示词二次编程：由 AI 生成可运行的高级提示词，再交给 AI 继续编程
* 从单一 `.py` 文件扩展到多文件企业级项目结构
* 迭代优化，目标是减少 99% 的重复劳动

#### 核心挑战

AI 自动编程的成败关键在于提示词的专业性、稳健性、准确性和安全性。
优秀程序员能够提供完整且可靠的技术栈，生成安全准确的目标代码；
初级程序员的提示词模糊，生成的代码也会模糊。

#### 数据与记录

* 每次的提示词会计入 `.json` 文件，用户可自由增删改查

#### 项目成果

本项目旨在验证 **AI 全自动编程替代轻量级重复劳动** 的可行性，目前成果相当惊艳，达到预期。

如果需要开源，请私聊我，关注我的 GitHub，过几天会发布源码以供交流。

---

#### Project Background

When large language models (LLMs) emerged, I began to wonder how they could reduce programmers’ workload in vertical applications. Later, I saw the rise of coding agents like **Cursor**. That made me think: could I build my own intelligent coding software?

#### Basic Concept

Steps of software development:

1. Build the project structure
2. Write the target files

Steps of learning software development:

1. Learn a new framework
2. Copy, paste, or migrate the new structure into use

#### Agent Design

In designing the coding agent, I followed this logic:

1. The agent script generates the project structure based on user prompts via an LLM
2. Then, it generates and executes the corresponding target code

At present, the project can only generate a single file, achieving only step two:
The agent script takes over the compiler and generates executable target code from user prompts using an LLM.

#### Future Plans

In the future, I will continue improving my full-stack capability, learning from mainstream coding agent projects, and adding new features:

* Add contextual engineering for project structure comprehension
* Mimic IDEA’s built-in Tongyi Lingma debugging capabilities
* Optimize erroneous requirements with reverse neural networks
* Simulate human learning by enabling LLMs to meta-learn new architectures
* Explore broader applications of AI coding agents

#### Technical Implementation

* Built on **DeepSeek**, targeting **PyCharm** and **Python**, similar to **Cursor**
* Users only need to provide requirements in the console to auto-generate target programs
* Principle: AI code generation → script writes to target files → auto execution and output

#### Value

* Beginner-friendly
* Saves professionals from repetitive lightweight tasks
* Enables modification of lightweight code or submission for advanced AI-driven re-development

#### Next Steps

* Secondary prompt programming: AI generates executable advanced prompts, then continues coding
* Expand from a single `.py` file to multi-file enterprise-level project structures
* Iterative optimization, aiming to reduce 99% of repetitive tasks

#### Core Challenge

The success of AI auto-programming depends on the professionalism, stability, accuracy, and safety of prompts.
Skilled programmers can provide a complete and reliable tech stack, resulting in accurate and safe code.
Inexperienced programmers, however, tend to write vague prompts, which lead to vague code.

#### Data & Records

* Each prompt is stored in a `.json` file, where users can perform CRUD operations

#### Project Outcome

This project aims to validate the feasibility of **AI auto-programming as a substitute for lightweight repetitive work**. The results so far are impressive and meet expectations.

If you’re interested in the open-source version, feel free to DM me and follow my GitHub — I will publish the source code soon for exchange and reference.
