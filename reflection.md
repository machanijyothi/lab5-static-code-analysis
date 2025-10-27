# Reflection

## **1. Which issues were the easiest to fix, and which were the hardest? Why?**
- The easiest issues to fix were adding **docstrings** and renaming functions to **snake_case**, as they only required minor code changes.  
- The hardest were replacing **`eval()`** safely and adding **file I/O exception handling**, which needed deeper understanding of the logic and error flow.

## **2. Did the static analysis tools report any false positives? If so, describe one example.**
- Yes, one **E501 (line too long)** warning appeared in Flake8.  
- It didn’t affect the program’s functionality or readability, so it was treated as a false positive for this lab.

## **3. How would you integrate static analysis tools into your actual software development workflow?**
- I would integrate **Pylint**, **Flake8**, and **Bandit** into a **Continuous Integration (CI)** pipeline using GitHub Actions.  
- I would also run these tools locally before every commit to ensure that all code meets quality and security standards.

## **4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**
- The code became **clearer, safer, and easier to maintain**.  
- Adding **logging** and **exception handling** improved reliability and error traceability.  
- Consistent naming and documentation enhanced **readability** and overall **professional quality** of the project.
