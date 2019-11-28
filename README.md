# python-3.8.0
My works related to Python programming language | version 3.8.0

<img src="python.png" height="100">

## Table of contents
1. [Introduction.](#introduction)
2. [Python principle.](#principle)
3. [Official references websites.](#references)
4. [Git & GitHub notes.](#git)
5. [Sublime text editor notes.](#sublime)
6. [JetBrains PyCharm text editor notes.](#pycharm)

<a name="introduction"></a>
## Introduction
Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of its features support functional programming and aspect-oriented programming (including by metaprogramming and metaobjects (magic methods)). Many other paradigms are supported via extensions, including design by contract and logic programming. Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management. It also features dynamic name resolution (late binding), which binds method and variable names during program execution.

<a name="principle"></a>
## Python principle
Beautiful is better than ugly. <br />
Explicit is better than implicit. <br />
Simple is better than complex. <br />
Complex is better than complicated. <br />
Flat is better than nested. <br />
Sparse is better than dense. <br />
Readability counts. <br />
Special cases aren't special enough to break the rules. <br />
Although practicality beats purity. <br />
Errors should never pass silently. <br />
Unless explicitly silenced. <br />
In the face of ambiguity, refuse the temptation to guess. <br />
There should be one—and preferably only one—obvious way to do it. <br />
Although that way may not be obvious at first unless you're Dutch. <br />
Now is better than never. <br />
Although never is often better than right now. <br />
If the implementation is hard to explain, it's a bad idea. <br />
If the implementation is easy to explain, it may be a good idea. <br />
Namespaces are one honking great idea—let's do more of those!

## Official references websites
<a name="references"></a>
Python official website : https://www.python.org

Python 3.8.0 official documentation : https://docs.python.org/3/
Python 3.8.0 documentation for Networking and Interprocess Communication : https://docs.python.org/3/library/ipc.html

Python IdleX text editor website : http://idlex.sourceforge.net

Python jobs : https://www.python.org/jobs/, https://www.pythonjobshq.com

<a name="github"></a>
## Git & GitHub notes
To unstage commits on Git, use the “git reset” command with the “–soft” option and specify the commit hash. Using the “–soft” argument, changes are kept in your working directory and index. As a consequence, your modifications are kept, they are just not in the Git repository anymore.
```
$ git reset --soft HEAD~1
$ git status
```

If a commit message contains unclear, incorrect, or sensitive information, you can amend it locally. You can also change a commit message to add missing information. After amend the message, view the log file to check again the commit message.
```
$ git commit --amend
$ git log --oneline -1
```

<a name="sublime"></a>
## Sublime text editor notes
From the Sublime menu, click **Tools** -> **Build System** -> **Python**. <br />
To run a program using Sublime text editor, press **[Ctrl]** + **[B]** buttons on your keyboard. <br />
To comment the selecting codes using Sublime text editor, press **[Ctrl]** + **[/]** buttons on your keyboard. <br />

To use terminal within Sublime text editor, follow the command shown in the YouTube video by **_Giovanni G._**, title **Use the terminal in Sublime text 3 with terminus**, by utilizing https://github.com/James231/Terminals-In-Sublime-Text GitHub repository. Run the terminal by pressing **[Alt]** + **[1]** buttons on your keyboard.

Official Sublime text editor website : https://www.sublimetext.com

<a name="pycharm"></a>
## JetBrains PyCharm text editor notes
When using JetBrains PyCharm as text editor for Python, to check all the changes made, press **[Alt]** + **[Shift]** + **[C]** buttons on your keyboard.  <br />
Copy and paste, duplicating text in JetBrains PyCharm is simply pressing **[Ctrl]** + **[D]** buttons on your keyboard, after the line that you wish to duplicate.  <br />

Official PyCharm text editor website : https://www.jetbrains.com/pycharm
