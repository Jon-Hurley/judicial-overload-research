import pandas as pd
import re

# Raw text pasted by user
raw_text = '''1754
1 texts
63 words
words + punctuation
1759
1 texts
30 words
words + punctuation
1760
1 texts
545 words
words + punctuation
1762
1 texts
224 words
words + punctuation
1763
1 texts
219 words
words + punctuation
1764
2 texts
1,538 words
words + punctuation
1766
1 texts
392 words
words + punctuation
1767
1 texts
724 words
words + punctuation
1768
1 texts
148 words
words + punctuation
1773
2 texts
425 words
words + punctuation
1776
1 texts
388 words
words + punctuation
1778
1 texts
615 words
words + punctuation
1779
1 texts
1,824 words
words + punctuation
1780
2 texts
1,297 words
words + punctuation
1781
6 texts
18,548 words
words + punctuation
1782
2 texts
1,561 words
words + punctuation
1783
2 texts
535 words
words + punctuation
1784
4 texts
2,193 words
words + punctuation
1785
5 texts
1,500 words
words + punctuation
1786
5 texts
2,340 words
words + punctuation
1787
3 texts
4,234 words
words + punctuation
1788
11 texts
6,233 words
words + punctuation
1789
6 texts
5,506 words
words + punctuation
1790
12 texts
9,858 words
words + punctuation
1791
4 texts
3,853 words
words + punctuation
1792
8 texts
16,564 words
words + punctuation
1793
4 texts
30,678 words
words + punctuation
1794
4 texts
1,905 words
words + punctuation
1795
6 texts
9,826 words
words + punctuation
1796
10 texts
14,203 words
words + punctuation
1797
8 texts
16,632 words
words + punctuation
1798
6 texts
21,129 words
words + punctuation
1799
13 texts
36,733 words
words + punctuation
1800
10 texts
13,049 words
words + punctuation
1801
9 texts
18,782 words
words + punctuation
1802
4 texts
10,701 words
words + punctuation
1803
21 texts
28,695 words
words + punctuation
1804
19 texts
35,331 words
words + punctuation
1805
25 texts
109,191 words
words + punctuation
1806
29 texts
84,980 words
words + punctuation
1807
19 texts
60,406 words
words + punctuation
1808
31 texts
77,713 words
words + punctuation
1809
40 texts
101,166 words
words + punctuation
1810
40 texts
108,912 words
words + punctuation
1812
38 texts
109,538 words
words + punctuation
1813
44 texts
92,058 words
words + punctuation
1814
43 texts
144,673 words
words + punctuation
1815
40 texts
163,551 words
words + punctuation
1816
42 texts
84,279 words
words + punctuation
1817
43 texts
62,149 words
words + punctuation
1818
36 texts
69,071 words
words + punctuation
1819
33 texts
188,116 words
words + punctuation
1820
27 texts
76,317 words
words + punctuation
1821
42 texts
149,145 words
words + punctuation
1822
31 texts
130,831 words
words + punctuation
1823
29 texts
85,334 words
words + punctuation
1824
41 texts
206,409 words
words + punctuation
1825
28 texts
106,216 words
words + punctuation
1826
32 texts
78,898 words
words + punctuation
1827
46 texts
202,756 words
words + punctuation
1828
55 texts
243,168 words
words + punctuation
1829
43 texts
192,083 words
words + punctuation
1830
59 texts
326,159 words
words + punctuation
1831
42 texts
224,478 words
words + punctuation
1832
53 texts
233,564 words
words + punctuation
1833
41 texts
221,275 words
words + punctuation
1834
62 texts
206,269 words
words + punctuation
1835
41 texts
234,221 words
words + punctuation
1836
52 texts
261,121 words
words + punctuation
1837
19 texts
272,772 words
words + punctuation
1838
41 texts
274,652 words
words + punctuation
1839
49 texts
219,293 words
words + punctuation
1840
43 texts
252,019 words
words + punctuation
1841
30 texts
203,287 words
words + punctuation
1842
44 texts
234,935 words
words + punctuation
1843
31 texts
115,595 words
words + punctuation
1844
38 texts
289,589 words
words + punctuation
1845
47 texts
350,622 words
words + punctuation
1846
46 texts
293,917 words
words + punctuation
1847
35 texts
238,974 words
words + punctuation
1848
36 texts
249,676 words
words + punctuation
1849
40 texts
374,496 words
words + punctuation
1850
159 texts
997,134 words
words + punctuation
1851
93 texts
477,910 words
words + punctuation
1852
53 texts
252,004 words
words + punctuation
1853
82 texts
481,099 words
words + punctuation
1854
68 texts
232,158 words
words + punctuation
1855
94 texts
228,021 words
words + punctuation
1856
60 texts
258,474 words
words + punctuation
1857
72 texts
231,796 words
words + punctuation
1858
66 texts
187,162 words
words + punctuation
1859
114 texts
310,731 words
words + punctuation
1860
65 texts
196,990 words
words + punctuation
1861
73 texts
143,690 words
words + punctuation
1862
41 texts
241,428 words
words + punctuation
1863
74 texts
169,633 words
words + punctuation
1864
64 texts
176,022 words
words + punctuation
1865
75 texts
173,411 words
words + punctuation
1866
132 texts
349,874 words
words + punctuation
1867
99 texts
189,815 words
words + punctuation
1868
114 texts
236,828 words
words + punctuation
1869
175 texts
322,776 words
words + punctuation
1870
161 texts
406,269 words
words + punctuation
1871
154 texts
300,111 words
words + punctuation
1872
175 texts
390,637 words
words + punctuation
1873
201 texts
462,159 words
words + punctuation
1874
193 texts
528,176 words
words + punctuation
1875
197 texts
475,739 words
words + punctuation
1876
223 texts
463,467 words
words + punctuation
1877
249 texts
508,158 words
words + punctuation
1878
207 texts
547,483 words
words + punctuation
1879
204 texts
502,542 words
words + punctuation
1880
218 texts
503,086 words
words + punctuation
1881
227 texts
494,042 words
words + punctuation
1882
77 texts
164,144 words
words + punctuation
1883
253 texts
578,039 words
words + punctuation
1884
274 texts
700,821 words
words + punctuation
1885
263 texts
588,121 words
words + punctuation
1886
270 texts
632,151 words
words + punctuation
1887
298 texts
761,643 words
words + punctuation
1888
291 texts
705,297 words
words + punctuation
1889
247 texts
552,305 words
words + punctuation
1890
277 texts
859,424 words
words + punctuation
1891
296 texts
775,416 words
words + punctuation
1892
248 texts
719,798 words
words + punctuation
1893
271 texts
734,158 words
words + punctuation
1894
259 texts
763,084 words
words + punctuation
1895
268 texts
865,425 words
words + punctuation
1896
244 texts
787,737 words
words + punctuation
1897
209 texts
772,466 words
words + punctuation
1898
171 texts
695,742 words
words + punctuation
1899
195 texts
692,799 words
words + punctuation
1900
227 texts
824,037 words
words + punctuation
1901
159 texts
605,348 words
words + punctuation
1902
201 texts
765,452 words
words + punctuation
1903
221 texts
588,153 words
words + punctuation
1904
205 texts
563,935 words
words + punctuation
1905
196 texts
504,516 words
words + punctuation
1906
180 texts
472,030 words
words + punctuation
1907
185 texts
469,322 words
words + punctuation
1908
176 texts
523,863 words
words + punctuation
1909
208 texts
441,380 words
words + punctuation
1910
206 texts
536,967 words
words + punctuation
1911
162 texts
405,890 words
words + punctuation
1912
221 texts
557,768 words
words + punctuation
1913
300 texts
732,800 words
words + punctuation
1914
269 texts
559,549 words
words + punctuation
1915
282 texts
630,290 words
words + punctuation
1916
237 texts
497,295 words
words + punctuation
1917
203 texts
405,575 words
words + punctuation
1918
191 texts
348,579 words
words + punctuation
1919
237 texts
435,656 words
words + punctuation
1920
190 texts
405,054 words
words + punctuation
1921
200 texts
394,059 words
words + punctuation
1922
190 texts
390,080 words
words + punctuation
1923
209 texts
409,983 words
words + punctuation
1924
207 texts
370,018 words
words + punctuation
1925
217 texts
374,457 words
words + punctuation
1926
214 texts
492,242 words
words + punctuation
1927
207 texts
419,587 words
words + punctuation
1928
158 texts
339,189 words
words + punctuation
1929
139 texts
303,942 words
words + punctuation
1930
143 texts
254,624 words
words + punctuation
1931
190 texts
383,780 words
words + punctuation
1932
172 texts
400,592 words
words + punctuation
1933
167 texts
435,315 words
words + punctuation
1934
182 texts
426,829 words
words + punctuation
1935
215 texts
448,158 words
words + punctuation
1936
159 texts
397,904 words
words + punctuation
1937
189 texts
435,005 words
words + punctuation
1938
189 texts
410,780 words
words + punctuation
1939
153 texts
400,060 words
words + punctuation
1940
142 texts
389,852 words
words + punctuation
1941
162 texts
415,165 words
words + punctuation
1942
157 texts
468,393 words
words + punctuation
1943
164 texts
542,854 words
words + punctuation
1944
134 texts
488,425 words
words + punctuation
1945
155 texts
625,343 words
words + punctuation
1946
142 texts
518,930 words
words + punctuation
1947
136 texts
590,250 words
words + punctuation
1948
116 texts
544,666 words
words + punctuation
1949
127 texts
539,964 words
words + punctuation
1950
94 texts
305,125 words
words + punctuation
1951
103 texts
309,672 words
words + punctuation
1952
116 texts
345,691 words
words + punctuation
1953
113 texts
324,710 words
words + punctuation
1954
77 texts
208,652 words
words + punctuation
1955
77 texts
223,524 words
words + punctuation
1956
110 texts
293,607 words
words + punctuation
1957
151 texts
415,509 words
words + punctuation
1958
199 texts
408,613 words
words + punctuation
1959
171 texts
436,331 words
words + punctuation
1960
169 texts
506,862 words
words + punctuation
1961
175 texts
675,683 words
words + punctuation
1962
180 texts
440,668 words
words + punctuation
1963
212 texts
588,036 words
words + punctuation
1964
228 texts
602,295 words
words + punctuation
1965
173 texts
484,333 words
words + punctuation
1966
170 texts
486,975 words
words + punctuation
1967
244 texts
613,481 words
words + punctuation
1968
224 texts
532,629 words
words + punctuation
1969
204 texts
505,773 words
words + punctuation
1970
201 texts
550,866 words
words + punctuation
1971
191 texts
703,489 words
words + punctuation
1972
237 texts
819,955 words
words + punctuation
1973
255 texts
946,102 words
words + punctuation
1974
225 texts
920,170 words
words + punctuation
1975
193 texts
668,476 words
words + punctuation
1976
214 texts
981,063 words
words + punctuation
1977
196 texts
806,782 words
words + punctuation
1978
213 texts
920,583 words
words + punctuation
1979
181 texts
820,237 words
words + punctuation
1980
206 texts
935,658 words
words + punctuation
1981
230 texts
879,021 words
words + punctuation
1982
226 texts
967,472 words
words + punctuation
1983
222 texts
1,045,913 words
words + punctuation
1984
238 texts
1,080,813 words
words + punctuation
1985
249 texts
1,103,222 words
words + punctuation
1986
230 texts
1,063,309 words
words + punctuation
1987
179 texts
927,516 words
words + punctuation
1988
191 texts
896,396 words
words + punctuation
1989
180 texts
1,012,532 words
words + punctuation
1990
153 texts
1,019,116 words
words + punctuation
1991
156 texts
846,760 words
words + punctuation
1992
123 texts
791,976 words
words + punctuation
1993
3055 texts
786,474 words
words + punctuation
1994
2051 texts
736,248 words
words + punctuation
1995
100 texts
697,444 words
words + punctuation
1996
86 texts
665,364 words
words + punctuation
1997
96 texts
681,083 words
words + punctuation
1998
88 texts
552,076 words
words + punctuation
1999
11 texts
146,455 words
words + punctuation
2000
46 texts
440,131 words
words + punctuation
2001
72 texts
466,537 words
words + punctuation
2002
7561 texts
661,940 words
words + punctuation
2003
8675 texts
831,422 words
words + punctuation
2004
6138 texts
635,517 words
words + punctuation
2005
4317 texts
497,950 words
words + punctuation
2006
71 texts
137,706 words
words + punctuation
2007
73 texts
158,385 words
words + punctuation
2008
73 texts
162,957 words
words + punctuation
2009
86 texts
149,691 words
words + punctuation
2010
83 texts
187,090 words
words + punctuation
2011
83 texts
158,930 words
words + punctuation
2012
77 texts
261,685 words
words + punctuation
2013
83 texts
278,233 words
words + punctuation
2014
73 texts
286,966 words
words + punctuation
2015
72 texts
217,049 words
words + punctuation
2016
80 texts
223,922 words
words + punctuation
2017
68 texts
163,930 words
words + punctuation
2018
91 texts
359,459 words
words + punctuation
2019
73 texts
269,120 words
words + punctuation
2020
68 texts
264,360 words
words + punctuation
2021
47 texts
155,185 words
words + punctuation'''

# Parse the text into structured rows
lines = raw_text.strip().split('\n')
data = []
for i in range(0, len(lines), 4):
    year = int(lines[i].strip())
    texts = int(re.search(r'\d+', lines[i+1]).group())
    words = int(re.sub(r'[^\d]', '', lines[i+2]))
    data.append({'year': year, 'texts': texts, 'words': words})

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_path = "courtdata/supreme_court_opinion_lengths.csv"
df.to_csv(output_path, index=False)

df.head()