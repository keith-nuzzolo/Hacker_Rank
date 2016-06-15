'''
Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters.

There are n chapters in Lisa's workbook, numbered from 1 to n.
The i-th chapter has ti problems, numbered from 1 to i.
Each page can hold up to k problems. There are no empty pages or unnecessary spaces, so only the last page of a chapter may contain fewer than k problems.
Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
The page number indexing starts at 1.
Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. Given the details for Lisa's workbook, can you count its number of special problems?

Input Format

The first line contains two integers n and k -the number of chapters and the maximum number of problems per page respectively.
The second line contains integers t1, t2, t3,...ti where  denotes the number of problems in the i-th chapter.

Sample Input:
5 3
4 2 6 1 10
Sample Output
4
'''
chapters, max_problems = [int(x) for x in input().rstrip().split()]
chapter_problems = [list(range(int(x))) for x in input().rstrip().split()]
special = page_num = 0
for chap in range(chapters):
    page_num += 1
    for problem in chapter_problems[chap]:
        if problem + 1 == page_num:
            special +=1
        if (problem +1) % max_problems == 0 and problem != chapter_problems[chap][-1]:
            page_num += 1
print(special)
