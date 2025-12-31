title: Final Submission Checklist 
template: page
status: hidden
slug: checklist

This page provides a checklist for common formatting issues in preparing the final version of your paper for SaTML. The checklist is largely taken from the excellent author instructions provided by [JMLR](https://www.jmlr.org/format/formatting-errors.html).  

## General

- Verify that you are using the exact template referenced in the [CFP](../participate-cfp/). This is a mandatory requirement.

- Verify that your submission adheres to the page limits and other requirements specified in the [CFP](../participate-cfp/) as well.

- Thoroughly proofread your source document to confirm that it requires no further revisions before submission.

## Main Text

- Prevent widows (a paragraph-ending line that starts at the top of the next page or column) and orphans (a paragraph-opening line that appears alone at the bottom of a page or column).

- Aim to avoid runts as well (a single word, part of a word, or a very short line that appears alone at the end of a paragraph).

- Avoid using references as nouns. Do not write phrases like “in [12].” brackets can be omitted and thus do not form proper nouns. Instead, use references as supporting information, e.g., “This algorithm achieves optimal results [12].”

- When referring to figures, tables, sections, and similar elements (e.g., “Figure&nbsp;1”, “Section&nbsp;2.1”), ensure that terms like “Figure” and “Section” are capitalized.

- At the end of your paper, the order of sections should be: Acknowledgments, References, then Appendices.

- Acknowledgments should be a unnumbered section.

- Appendix section number should be a letter. You can use `\appendix` followed by a regular `\section` command to format appendices

## Headings, Figures and Tables

- Use title case for the title and all section and subsection headings. Capitalize the first letter of each word, except for small words like “and” and “or.”

- Place floats (e.g., `figure` and `table` environments) at the top or bottom of the page whenever possible. Ensure pages with multiple floats are arranged neatly.

- Position floats as close as possible to the point where they are first referenced in the text.

- Center figures and tables within their respective environments.

- Place captions *below* figures and *above* tables, as this is the standard convention.

## Math

- Math in formal writing should be punctuated as if the extra space is not there, for example, displayed equations should usually be followed by a comma or a period, depending on the surrounding text.

- Before displayed equations, punctuation (e.g., ":") is not necessary unless you would use the same punctuation if the equation were not there.

- Proofs should end with a filled box.

- Theorems, Lemmas, etc., should be labeled like Theorem&nbsp;1, Theorem&nbsp;2, not as Theorem&nbsp;2.1, Theorem&nbsp;2.2.

## References

- It is preferable to cite published conference and journal papers, rather than tech reports.

- Please cite conference titles consistently. We do not have a enforced style for conference names, but whichever style you choose, be consistent.

## Misc

- Footnote markers should follow punctuation.

- When using dashes in text, please use `---` instead of `--`, with no space before or after the dash---like this.

- Use `\url` commands to reference URLs in papers. This causes hyperref to make the hyperlinks work nicely.

- You may also check out Andreas Zeller's [LaTeX Korrektor](https://www.youtube.com/watch?v=EhsMdQQJ_bE&list=PL6dh-k4faL8qTs8LQOsfbY70owETfWy5L) to learn about common LaTeX mistakes.

- Further advice on LaTeX writing is available from Diomidis Spinellis' [tutorial](https://github.com/dspinellis/latex-advice)
