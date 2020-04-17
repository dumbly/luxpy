# -*- coding: utf-8 -*-

########################################################################
# <LUXPY: a Python package for lighting and color science.>
# Copyright (C) <2017>  <Kevin A.G. Smet> (ksmet1977 at gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#########################################################################

"""
Module for loading light source (spd) and reflectance (rfl) spectra databases
=============================================================================

 :_S_PATH: Path to light source spectra data.

 :_R_PATH: Path to with spectral reflectance data

 :_IESTM3015: Database with spectral reflectances related to and light source 
            spectra contained excel calculator of IES TM30-15 publication.
            
 :_IESTM3018: Database with spectral reflectances related to and light source 
            spectra contained excel calculator of IES TM30-18 publication.

 :_IESTM3015_S: Database with only light source spectra contained in the 
              IES TM30-15 excel calculator.
              
 :_IESTM3018_S: Database with only light source spectra contained in the 
              IES TM30-18 excel calculator.

 :_CIE_ILLUMINANTS: | Database with CIE illuminants: 
                    | * 'E', 'D65', 'A', 'C',
                    | * 'F1', 'F2', 'F3', 'F4', 'F5', 'F6',
                      'F7', 'F8', 'F9', 'F10', 'F11', 'F12'
                      
 :_CIE_E, _CIE_D65, _CIE_A, ',_CIE_B', _CIE_C, _CIE_F4: Some CIE illuminants for easy use.

 :_CRI_RFL: | Database with spectral reflectance functions for various 
              color rendition calculators:
            | * `CIE 13.3-1995 (8, 14 munsell samples) <http://www.cie.co.at/index.php/index.php?i_ca_id=303>`_
            | * `CIE 224:2015 (99 set) <http://www.cie.co.at/index.php?i_ca_id=1027>`_
            | * `CRI2012 (HL17 & HL1000 spectrally uniform and 210 real samples) <http://journals.sagepub.com/doi/abs/10.1177/1477153513481375>`_
            | * `IES TM30 (99, 4880 sepctrally uniform samples) <https://www.ies.org/store/technical-memoranda/ies-method-for-evaluating-light-source-color-rendition>`_
            | * `MCRI (10 familiar object set) <http://www.sciencedirect.com/science/article/pii/S0378778812000837>`_
            | * `CQS (v7.5 and v9.0 sets) <http://spie.org/Publications/Journal/10.1117/1.3360335>`_

 :_MUNSELL: Database (dict) with 1269 Munsell spectral reflectance functions 
            and Value (V), Chroma (C), hue (h) and (ab) specifications.
           
 :_RFL: | Database (dict) with RFLs, including:
        | * all those in _CRI_RFL, 
        | * the 1269 Matt Munsell samples (see also _MUNSELL),
        | * the 24 Macbeth ColorChecker samples,
        | * the 215 samples proposed by Opstelten, J.J. , 1983, The establishment of a representative set of test colours
        |   for the specification of the colour rendering properties of light sources, CIE-20th session, Amsterdam. 
        | * the 114120 RFLs from `(capbone.com/spectral-reflectance-database/)<114120 RFLs from https://capbone.com/spectral-reflectance-database/>`_
            
.. codeauthor:: Kevin A.G. Smet (ksmet1977 at gmail.com)
"""
from luxpy import np, copy, _PKG_PATH, _SEP, getdata
__all__ = ['_R_PATH','_S_PATH', '_IESTM3015','_IESTM3015_S',
           '_IESTM3018','_IESTM3018_S','_CRI_RFL','_CIE_ILLUMINANTS',
           '_CIE_E', '_CIE_D65', '_CIE_A','_CIE_B', '_CIE_C', '_CIE_F4',
           '_CIE_F_1_12','_CIE_F3_1_15','_CIE_HP_1_5',
           '_RFL', '_MUNSELL']


#_C_dir = _PKG_PATH + _SEP + 'data'+ _SEP + 'cmfs' + _SEP #folder with cmf data
_S_PATH = _PKG_PATH + _SEP + 'data'+ _SEP + 'spds' + _SEP #folder with spd data
_R_PATH = _PKG_PATH + _SEP + 'data'+ _SEP + 'rfls' + _SEP #folder with rfl data



###############################################################################
# spectral power distributions:
    
# load TM30 spd data base:
_IESTM3015 = {'S': {'data': getdata(_S_PATH + 'IESTM30_15_Sspds.dat',kind='np').transpose()}}
_IESTM3015['S']['info'] = getdata(_S_PATH + 'IESTM30_15_Sinfo.txt',kind='np',header='infer',verbosity = False)
_IESTM3015_S = _IESTM3015['S']

_IESTM3018 = {'S': {'data': getdata(_S_PATH + 'IESTM30_15_Sspds.dat',kind='np').transpose()}}
_IESTM3018['S']['info'] = getdata(_S_PATH + 'IESTM30_15_Sinfo.txt',kind='np',header='infer',verbosity = False)
_IESTM3018_S = _IESTM3018['S']





#------------------------------------------------------------------------------
# Illuminant library: set some typical CIE illuminants:
E = np.array([np.linspace(360,830,471),np.ones(471)])
_CIE_E = E.copy()

#D65 = np.array([[380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780],
#              [49.98,50.33,50.84,51.42,51.94,52.31,52.47,52.58,52.84,53.46,54.65,56.56,59.08,62.05,65.31,68.7,72.06,75.26,78.19,80.73,82.75,84.2,85.18,85.89,86.47,87.12,87.95,88.91,89.89,90.78,91.49,91.92,92.15,92.26,92.33,92.46,92.69,92.99,93.26,93.44,93.43,93.18,92.7,92,91.11,90.06,88.89,87.78,86.91,86.48,86.68,87.64,89.23,91.24,93.49,95.77,97.93,99.92,101.7,103.4,104.9,106.2,107.4,108.5,109.7,110.9,112.3,113.7,115,116.2,117,117.5,117.6,117.6,117.5,117.4,117.4,117.6,117.7,117.8,117.8,117.7,117.4,117.1,116.7,116.3,115.9,115.6,115.3,115,114.9,114.8,114.8,115,115.2,115.4,115.7,115.9,116.1,116.1,115.9,115.5,114.9,114.1,113.3,112.4,111.5,110.6,109.8,109.2,108.8,108.6,108.6,108.7,108.9,109.1,109.2,109.3,109.4,109.4,109.4,109.2,109.1,108.9,108.7,108.6,108.4,108.3,108.1,108,107.8,107.6,107.3,107,106.7,106.3,105.9,105.5,105.1,104.9,104.8,104.9,105.1,105.4,105.8,106.2,106.7,107.1,107.4,107.6,107.7,107.6,107.3,106.9,106.5,106,105.6,105.2,104.9,104.6,104.4,104.3,104.2,104.2,104.2,104.2,104.3,104.3,104.3,104.2,104,103.8,103.4,103,102.5,102,101.6,101.2,100.8,100.4,100,99.64,99.29,98.93,98.56,98.17,97.76,97.34,96.95,96.61,96.33,96.15,96.04,96,96.01,96.06,96.13,96.19,96.18,96.06,95.79,95.33,94.71,93.96,93.13,92.24,91.33,90.47,89.7,89.08,88.69,88.54,88.59,88.79,89.06,89.35,89.58,89.76,89.89,89.97,90.01,90,89.96,89.9,89.85,89.8,89.78,89.76,89.74,89.69,89.6,89.45,89.27,89.06,88.85,88.65,88.48,88.32,88.16,87.96,87.7,87.37,86.97,86.52,86.02,85.49,84.95,84.43,83.95,83.56,83.29,83.15,83.14,83.21,83.34,83.49,83.64,83.76,83.82,83.81,83.7,83.48,83.16,82.77,82.33,81.86,81.4,80.95,80.56,80.24,80.03,79.93,79.92,79.98,80.06,80.12,80.15,80.15,80.15,80.16,80.21,80.32,80.48,80.69,80.95,81.25,81.58,81.9,82.15,82.3,82.28,82.06,81.7,81.23,80.74,80.28,79.89,79.54,79.19,78.79,78.28,77.64,76.88,76,75.04,74,72.93,71.88,70.95,70.2,69.72,69.56,69.67,69.95,70.31,70.67,70.95,71.16,71.33,71.47,71.61,71.77,71.96,72.22,72.55,72.98,73.5,74.02,74.41,74.56,74.35,73.69,72.64,71.28,69.7,67.98,66.22,64.56,63.14,62.1,61.6,61.73,62.38,63.37,64.55,65.74,66.83,67.77,68.59,69.29,69.89,70.39,70.84,71.31,71.84,72.49,73.27,74.08,74.75,75.14,75.09,74.5,73.47,72.17,70.74,69.34,68.09,66.95,65.87,64.77,63.59,62.27,60.77,59.08,57.17,55.01,52.63,50.28,48.27,46.88,46.42,47.09,48.72,51.03,53.75,56.61,59.36,61.86,64.01,65.69,66.81,67.28,67.21,66.73,65.98,65.09,64.21,63.46,62.98,62.91,63.38]])
D65 = getdata(_S_PATH + 'D65.dat',kind='np').T
_CIE_D65 = D65.copy()

#A = np.array([[380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780],
#               [9.795,10.01,10.23,10.45,10.67,10.9,11.13,11.36,11.6,11.84,12.09,12.33,12.58,12.84,13.09,13.35,13.62,13.89,14.16,14.43,14.71,14.99,15.27,15.56,15.85,16.15,16.45,16.75,17.05,17.36,17.68,17.99,18.31,18.63,18.96,19.29,19.62,19.96,20.3,20.65,21,21.35,21.7,22.06,22.42,22.79,23.16,23.53,23.91,24.29,24.67,25.06,25.45,25.84,26.24,26.64,27.05,27.46,27.87,28.28,28.7,29.13,29.55,29.98,30.41,30.85,31.29,31.73,32.18,32.63,33.09,33.54,34,34.47,34.94,35.41,35.88,36.36,36.84,37.32,37.81,38.3,38.8,39.3,39.8,40.3,40.81,41.32,41.83,42.35,42.87,43.39,43.92,44.45,44.98,45.52,46.06,46.6,47.14,47.69,48.24,48.8,49.35,49.91,50.48,51.04,51.61,52.18,52.76,53.33,53.91,54.5,55.08,55.67,56.26,56.85,57.45,58.05,58.65,59.26,59.86,60.47,61.08,61.7,62.31,62.93,63.55,64.18,64.8,65.43,66.06,66.7,67.33,67.97,68.61,69.25,69.9,70.54,71.19,71.84,72.5,73.15,73.81,74.47,75.13,75.79,76.45,77.12,77.79,78.46,79.13,79.81,80.48,81.16,81.84,82.52,83.2,83.89,84.57,85.26,85.95,86.64,87.33,88.02,88.72,89.41,90.11,90.81,91.51,92.21,92.91,93.62,94.32,95.03,95.73,96.44,97.15,97.86,98.57,99.29,100,100.7,101.4,102.2,102.9,103.6,104.3,105,105.7,106.5,107.2,107.9,108.6,109.3,110.1,110.8,111.5,112.3,113,113.7,114.4,115.2,115.9,116.6,117.3,118.1,118.8,119.5,120.3,121,121.7,122.5,123.2,123.9,124.7,125.4,126.1,126.8,127.6,128.3,129,129.8,130.5,131.2,132,132.7,133.4,134.2,134.9,135.6,136.3,137.1,137.8,138.5,139.3,140,140.7,141.4,142.2,142.9,143.6,144.3,145.1,145.8,146.5,147.2,148,148.7,149.4,150.1,150.8,151.6,152.3,153,153.7,154.4,155.1,155.8,156.6,157.3,158,158.7,159.4,160.1,160.8,161.5,162.2,162.9,163.6,164.3,165,165.7,166.4,167.1,167.8,168.5,169.2,169.9,170.6,171.3,172,172.7,173.3,174,174.7,175.4,176.1,176.7,177.4,178.1,178.8,179.4,180.1,180.8,181.4,182.1,182.8,183.4,184.1,184.8,185.4,186.1,186.7,187.4,188.1,188.7,189.3,190,190.6,191.3,191.9,192.6,193.2,193.8,194.5,195.1,195.8,196.4,197,197.6,198.3,198.9,199.5,200.1,200.7,201.4,202,202.6,203.2,203.8,204.4,205,205.6,206.2,206.8,207.4,208,208.6,209.2,209.8,210.4,210.9,211.5,212.1,212.7,213.3,213.8,214.4,215,215.6,216.1,216.7,217.3,217.8,218.4,218.9,219.5,220,220.6,221.1,221.7,222.2,222.8,223.3,223.8,224.4,224.9,225.4,225.9,226.5,227,227.5,228,228.6,229.1,229.6,230.1,230.6,231.1,231.6,232.1,232.6,233.1,233.6,234.1,234.6,235.1,235.6,236.1,236.5,237,237.5,238,238.4,238.9,239.4,239.8,240.3,240.8,241.2,241.7]])
A = getdata(_S_PATH + 'A.dat',kind='np').T
_CIE_A = A.copy()

B = np.array([[360.0,361.0,362.0,363.0,364.0,365.0,366.0,367.0,368.0,369.0,370.0,371.0,372.0,373.0,374.0,375.0,376.0,377.0,378.0,379.0,380.0,381.0,382.0,383.0,384.0,385.0,386.0,387.0,388.0,389.0,390.0,391.0,392.0,393.0,394.0,395.0,396.0,397.0,398.0,399.0,400.0,401.0,402.0,403.0,404.0,405.0,406.0,407.0,408.0,409.0,410.0,411.0,412.0,413.0,414.0,415.0,416.0,417.0,418.0,419.0,420.0,421.0,422.0,423.0,424.0,425.0,426.0,427.0,428.0,429.0,430.0,431.0,432.0,433.0,434.0,435.0,436.0,437.0,438.0,439.0,440.0,441.0,442.0,443.0,444.0,445.0,446.0,447.0,448.0,449.0,450.0,451.0,452.0,453.0,454.0,455.0,456.0,457.0,458.0,459.0,460.0,461.0,462.0,463.0,464.0,465.0,466.0,467.0,468.0,469.0,470.0,471.0,472.0,473.0,474.0,475.0,476.0,477.0,478.0,479.0,480.0,481.0,482.0,483.0,484.0,485.0,486.0,487.0,488.0,489.0,490.0,491.0,492.0,493.0,494.0,495.0,496.0,497.0,498.0,499.0,500.0,501.0,502.0,503.0,504.0,505.0,506.0,507.0,508.0,509.0,510.0,511.0,512.0,513.0,514.0,515.0,516.0,517.0,518.0,519.0,520.0,521.0,522.0,523.0,524.0,525.0,526.0,527.0,528.0,529.0,530.0,531.0,532.0,533.0,534.0,535.0,536.0,537.0,538.0,539.0,540.0,541.0,542.0,543.0,544.0,545.0,546.0,547.0,548.0,549.0,550.0,551.0,552.0,553.0,554.0,555.0,556.0,557.0,558.0,559.0,560.0,561.0,562.0,563.0,564.0,565.0,566.0,567.0,568.0,569.0,570.0,571.0,572.0,573.0,574.0,575.0,576.0,577.0,578.0,579.0,580.0,581.0,582.0,583.0,584.0,585.0,586.0,587.0,588.0,589.0,590.0,591.0,592.0,593.0,594.0,595.0,596.0,597.0,598.0,599.0,600.0,601.0,602.0,603.0,604.0,605.0,606.0,607.0,608.0,609.0,610.0,611.0,612.0,613.0,614.0,615.0,616.0,617.0,618.0,619.0,620.0,621.0,622.0,623.0,624.0,625.0,626.0,627.0,628.0,629.0,630.0,631.0,632.0,633.0,634.0,635.0,636.0,637.0,638.0,639.0,640.0,641.0,642.0,643.0,644.0,645.0,646.0,647.0,648.0,649.0,650.0,651.0,652.0,653.0,654.0,655.0,656.0,657.0,658.0,659.0,660.0,661.0,662.0,663.0,664.0,665.0,666.0,667.0,668.0,669.0,670.0,671.0,672.0,673.0,674.0,675.0,676.0,677.0,678.0,679.0,680.0,681.0,682.0,683.0,684.0,685.0,686.0,687.0,688.0,689.0,690.0,691.0,692.0,693.0,694.0,695.0,696.0,697.0,698.0,699.0,700.0,701.0,702.0,703.0,704.0,705.0,706.0,707.0,708.0,709.0,710.0,711.0,712.0,713.0,714.0,715.0,716.0,717.0,718.0,719.0,720.0,721.0,722.0,723.0,724.0,725.0,726.0,727.0,728.0,729.0,730.0,731.0,732.0,733.0,734.0,735.0,736.0,737.0,738.0,739.0,740.0,741.0,742.0,743.0,744.0,745.0,746.0,747.0,748.0,749.0,750.0,751.0,752.0,753.0,754.0,755.0,756.0,757.0,758.0,759.0,760.0,761.0,762.0,763.0,764.0,765.0,766.0,767.0,768.0,769.0,770.0,771.0,772.0,773.0,774.0,775.0,776.0,777.0,778.0,779.0,780.0,781.0,782.0,783.0,784.0,785.0,786.0,787.0,788.0,789.0,790.0,791.0,792.0,793.0,794.0,795.0,796.0,797.0,798.0,799.0,800.0,801.0,802.0,803.0,804.0,805.0,806.0,807.0,808.0,809.0,810.0,811.0,812.0,813.0,814.0,815.0,816.0,817.0,818.0,819.0,820.0,821.0,822.0,823.0,824.0,825.0,826.0,827.0,828.0,829.0,830.0],
			  [9.6,10.16,10.72,11.28,11.84,12.4,12.96,13.52,14.08,14.64,15.2,15.92,16.64,17.36,18.08,18.8,19.52,20.24,20.96,21.68,22.4,23.29,24.18,25.07,25.96,26.85,27.74,28.63,29.52,30.41,31.3,32.28,33.25,34.23,35.2,36.18,37.2,38.23,39.25,40.28,41.3,42.36,43.43,44.49,45.56,46.62,47.72,48.81,49.91,51.0,52.1,53.22,54.34,55.46,56.58,57.7,58.8,59.9,61.0,62.1,63.2,64.23,65.27,66.3,67.34,68.37,69.32,70.26,71.21,72.15,73.1,73.94,74.78,75.63,76.47,77.31,78.01,78.71,79.4,80.1,80.8,81.33,81.86,82.38,82.91,83.44,83.83,84.22,84.62,85.01,85.4,85.7,85.99,86.29,86.58,86.88,87.16,87.45,87.73,88.02,88.3,88.66,89.01,89.37,89.72,90.08,90.46,90.85,91.23,91.62,92.0,92.35,92.7,93.05,93.4,93.75,94.04,94.33,94.62,94.91,95.2,95.41,95.61,95.82,96.02,96.23,96.28,96.34,96.39,96.45,96.5,96.34,96.18,96.03,95.87,95.71,95.41,95.11,94.8,94.5,94.2,93.83,93.47,93.1,92.74,92.37,92.04,91.7,91.37,91.03,90.7,90.55,90.4,90.25,90.1,89.95,89.86,89.77,89.68,89.59,89.5,89.69,89.87,90.06,90.24,90.43,90.78,91.14,91.49,91.85,92.2,92.65,93.1,93.56,94.01,94.46,94.95,95.44,95.92,96.41,96.9,97.35,97.8,98.26,98.71,99.16,99.53,99.9,100.26,100.63,101.0,101.24,101.48,101.72,101.96,102.2,102.32,102.44,102.56,102.68,102.8,102.82,102.85,102.87,102.9,102.92,102.86,102.79,102.73,102.66,102.6,102.46,102.32,102.18,102.04,101.9,101.72,101.54,101.36,101.18,101.0,100.81,100.63,100.44,100.26,100.07,99.9,99.72,99.55,99.37,99.2,99.05,98.9,98.74,98.59,98.44,98.35,98.26,98.18,98.09,98.0,98.02,98.03,98.05,98.06,98.08,98.16,98.25,98.33,98.42,98.5,98.61,98.72,98.84,98.95,99.06,99.19,99.32,99.44,99.57,99.7,99.83,99.96,100.1,100.23,100.36,100.49,100.62,100.74,100.87,101.0,101.11,101.22,101.34,101.45,101.56,101.69,101.82,101.94,102.07,102.2,102.37,102.54,102.71,102.88,103.05,103.22,103.39,103.56,103.73,103.9,104.04,104.18,104.31,104.45,104.59,104.67,104.75,104.84,104.92,105.0,105.02,105.03,105.05,105.06,105.08,105.04,105.01,104.97,104.94,104.9,104.83,104.76,104.69,104.62,104.55,104.42,104.29,104.16,104.03,103.9,103.69,103.48,103.26,103.05,102.84,102.59,102.34,102.1,101.85,101.6,101.36,101.11,100.87,100.62,100.38,100.12,99.87,99.61,99.36,99.1,98.82,98.54,98.26,97.98,97.7,97.4,97.1,96.8,96.5,96.2,95.88,95.56,95.24,94.92,94.6,94.26,93.92,93.58,93.24,92.9,92.54,92.18,91.82,91.46,91.1,90.76,90.42,90.08,89.74,89.4,89.12,88.84,88.56,88.28,88.0,87.78,87.56,87.34,87.12,86.9,86.7,86.5,86.3,86.1,85.9,85.76,85.62,85.48,85.34,85.2,85.12,85.04,84.96,84.88,84.8,84.78,84.76,84.74,84.72,84.7,84.74,84.78,84.82,84.86,84.9,85.0,85.1,85.2,85.3,85.4,85.54,85.68,85.82,85.96,86.1,86.28,86.46,86.64,86.82,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0,87.0]])
_CIE_B = B.copy()

C = np.array([[360.0,361.0,362.0,363.0,364.0,365.0,366.0,367.0,368.0,369.0,370.0,371.0,372.0,373.0,374.0,375.0,376.0,377.0,378.0,379.0,380.0,381.0,382.0,383.0,384.0,385.0,386.0,387.0,388.0,389.0,390.0,391.0,392.0,393.0,394.0,395.0,396.0,397.0,398.0,399.0,400.0,401.0,402.0,403.0,404.0,405.0,406.0,407.0,408.0,409.0,410.0,411.0,412.0,413.0,414.0,415.0,416.0,417.0,418.0,419.0,420.0,421.0,422.0,423.0,424.0,425.0,426.0,427.0,428.0,429.0,430.0,431.0,432.0,433.0,434.0,435.0,436.0,437.0,438.0,439.0,440.0,441.0,442.0,443.0,444.0,445.0,446.0,447.0,448.0,449.0,450.0,451.0,452.0,453.0,454.0,455.0,456.0,457.0,458.0,459.0,460.0,461.0,462.0,463.0,464.0,465.0,466.0,467.0,468.0,469.0,470.0,471.0,472.0,473.0,474.0,475.0,476.0,477.0,478.0,479.0,480.0,481.0,482.0,483.0,484.0,485.0,486.0,487.0,488.0,489.0,490.0,491.0,492.0,493.0,494.0,495.0,496.0,497.0,498.0,499.0,500.0,501.0,502.0,503.0,504.0,505.0,506.0,507.0,508.0,509.0,510.0,511.0,512.0,513.0,514.0,515.0,516.0,517.0,518.0,519.0,520.0,521.0,522.0,523.0,524.0,525.0,526.0,527.0,528.0,529.0,530.0,531.0,532.0,533.0,534.0,535.0,536.0,537.0,538.0,539.0,540.0,541.0,542.0,543.0,544.0,545.0,546.0,547.0,548.0,549.0,550.0,551.0,552.0,553.0,554.0,555.0,556.0,557.0,558.0,559.0,560.0,561.0,562.0,563.0,564.0,565.0,566.0,567.0,568.0,569.0,570.0,571.0,572.0,573.0,574.0,575.0,576.0,577.0,578.0,579.0,580.0,581.0,582.0,583.0,584.0,585.0,586.0,587.0,588.0,589.0,590.0,591.0,592.0,593.0,594.0,595.0,596.0,597.0,598.0,599.0,600.0,601.0,602.0,603.0,604.0,605.0,606.0,607.0,608.0,609.0,610.0,611.0,612.0,613.0,614.0,615.0,616.0,617.0,618.0,619.0,620.0,621.0,622.0,623.0,624.0,625.0,626.0,627.0,628.0,629.0,630.0,631.0,632.0,633.0,634.0,635.0,636.0,637.0,638.0,639.0,640.0,641.0,642.0,643.0,644.0,645.0,646.0,647.0,648.0,649.0,650.0,651.0,652.0,653.0,654.0,655.0,656.0,657.0,658.0,659.0,660.0,661.0,662.0,663.0,664.0,665.0,666.0,667.0,668.0,669.0,670.0,671.0,672.0,673.0,674.0,675.0,676.0,677.0,678.0,679.0,680.0,681.0,682.0,683.0,684.0,685.0,686.0,687.0,688.0,689.0,690.0,691.0,692.0,693.0,694.0,695.0,696.0,697.0,698.0,699.0,700.0,701.0,702.0,703.0,704.0,705.0,706.0,707.0,708.0,709.0,710.0,711.0,712.0,713.0,714.0,715.0,716.0,717.0,718.0,719.0,720.0,721.0,722.0,723.0,724.0,725.0,726.0,727.0,728.0,729.0,730.0,731.0,732.0,733.0,734.0,735.0,736.0,737.0,738.0,739.0,740.0,741.0,742.0,743.0,744.0,745.0,746.0,747.0,748.0,749.0,750.0,751.0,752.0,753.0,754.0,755.0,756.0,757.0,758.0,759.0,760.0,761.0,762.0,763.0,764.0,765.0,766.0,767.0,768.0,769.0,770.0,771.0,772.0,773.0,774.0,775.0,776.0,777.0,778.0,779.0,780.0,781.0,782.0,783.0,784.0,785.0,786.0,787.0,788.0,789.0,790.0,791.0,792.0,793.0,794.0,795.0,796.0,797.0,798.0,799.0,800.0,801.0,802.0,803.0,804.0,805.0,806.0,807.0,808.0,809.0,810.0,811.0,812.0,813.0,814.0,815.0,816.0,817.0,818.0,819.0,820.0,821.0,822.0,823.0,824.0,825.0,826.0,827.0,828.0,829.0,830.0],
			  [12.9,13.76,14.62,15.48,16.34,17.2,18.04,18.88,19.72,20.56,21.4,22.62,23.84,25.06,26.28,27.5,28.6,29.7,30.8,31.9,33.0,34.38,35.77,37.15,38.54,39.92,41.42,42.91,44.41,45.9,47.4,48.95,50.51,52.06,53.62,55.17,56.8,58.42,60.05,61.67,63.3,65.0,66.7,68.41,70.11,71.81,73.57,75.33,77.08,78.84,80.6,82.39,84.17,85.96,87.74,89.53,91.24,92.96,94.67,96.39,98.1,99.64,101.18,102.72,104.26,105.8,107.12,108.44,109.76,111.08,112.4,113.47,114.54,115.61,116.68,117.75,118.5,119.25,120.0,120.75,121.5,121.89,122.28,122.67,123.06,123.45,123.56,123.67,123.78,123.89,124.0,123.92,123.84,123.76,123.68,123.6,123.5,123.4,123.3,123.2,123.1,123.14,123.18,123.22,123.26,123.3,123.4,123.5,123.6,123.7,123.8,123.86,123.92,123.97,124.03,124.09,124.05,124.01,123.98,123.94,123.9,123.7,123.51,123.31,123.12,122.92,122.48,122.03,121.59,121.14,120.7,119.94,119.18,118.42,117.66,116.9,115.94,114.98,114.02,113.06,112.1,111.08,110.05,109.03,108.0,106.98,106.04,105.11,104.17,103.24,102.3,101.6,100.9,100.21,99.51,98.81,98.43,98.05,97.66,97.28,96.9,96.88,96.85,96.83,96.8,96.78,97.02,97.27,97.51,97.76,98.0,98.39,98.78,99.16,99.55,99.94,100.37,100.8,101.24,101.67,102.1,102.47,102.84,103.21,103.58,103.95,104.2,104.45,104.7,104.95,105.2,105.29,105.39,105.48,105.58,105.67,105.6,105.52,105.45,105.37,105.3,105.06,104.82,104.59,104.35,104.11,103.75,103.39,103.02,102.66,102.3,101.87,101.44,101.01,100.58,100.15,99.68,99.21,98.74,98.27,97.8,97.33,96.85,96.38,95.9,95.43,94.98,94.54,94.09,93.65,93.2,92.8,92.41,92.01,91.62,91.22,90.92,90.61,90.31,90.0,89.7,89.53,89.35,89.18,89.0,88.83,88.74,88.66,88.57,88.49,88.4,88.36,88.32,88.27,88.23,88.19,88.17,88.15,88.14,88.12,88.1,88.09,88.08,88.08,88.07,88.06,88.05,88.04,88.02,88.01,88.0,87.97,87.94,87.92,87.89,87.86,87.85,87.84,87.82,87.81,87.8,87.84,87.88,87.91,87.95,87.99,88.03,88.07,88.12,88.16,88.2,88.2,88.2,88.2,88.2,88.2,88.14,88.08,88.02,87.96,87.9,87.76,87.63,87.49,87.36,87.22,87.04,86.85,86.67,86.48,86.3,86.1,85.9,85.7,85.5,85.3,85.04,84.78,84.52,84.26,84.0,83.64,83.28,82.93,82.57,82.21,81.81,81.41,81.0,80.6,80.2,79.81,79.42,79.02,78.63,78.24,77.85,77.46,77.08,76.69,76.3,75.91,75.52,75.14,74.75,74.36,73.97,73.58,73.18,72.79,72.4,72.0,71.6,71.2,70.8,70.4,69.98,69.56,69.14,68.72,68.3,67.9,67.5,67.1,66.7,66.3,65.92,65.54,65.16,64.78,64.4,64.08,63.76,63.44,63.12,62.8,62.54,62.28,62.02,61.76,61.5,61.24,60.98,60.72,60.46,60.2,60.0,59.8,59.6,59.4,59.2,59.06,58.92,58.78,58.64,58.5,58.42,58.34,58.26,58.18,58.1,58.08,58.06,58.04,58.02,58.0,58.04,58.08,58.12,58.16,58.2,58.26,58.32,58.38,58.44,58.5,58.62,58.74,58.86,58.98,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1,59.1]])
_CIE_C = C.copy()

_CIE_F_1_12 = getdata(_S_PATH + 'CIE_F_1to12.csv',kind='np').T
_CIE_F_1_12_dict = {'F{:1.0f}'.format(i+1):np.vstack((_CIE_F_1_12[0],_CIE_F_1_12[i+1])) for i in range(12)}

_CIE_F3_1_15 = getdata(_S_PATH + 'CIE_F3_1to15.csv',kind='np').T
_CIE_F3_1_15_dict = {'F3.{:1.0f}'.format(i+1):np.vstack((_CIE_F3_1_15[0],_CIE_F3_1_15[i+1])) for i in range(15)}

_CIE_HP_1_5 = getdata(_S_PATH + 'CIE_F3_1to15.csv',kind='np').T
_CIE_HP_1_5_dict = {'HP{:1.0f}'.format(i+1):np.vstack((_CIE_HP_1_5[0],_CIE_HP_1_5[i+1])) for i in range(5)}

_CIE_ILLUMINANTS = {'E':E,'D65':D65,'A':A,'B':B,'C':C}
_CIE_ILLUMINANTS.update(_CIE_F_1_12_dict)				  
_CIE_ILLUMINANTS.update(_CIE_F3_1_15_dict)
_CIE_ILLUMINANTS.update(_CIE_HP_1_5_dict)
_CIE_ILLUMINANTS['types'] = list(_CIE_ILLUMINANTS.keys())

_CIE_F4 = _CIE_ILLUMINANTS['F4']

del E, D65, A, B, C, _CIE_F_1_12_dict , _CIE_F3_1_15_dict, _CIE_HP_1_5_dict, 


###############################################################################
# spectral reflectance functions:

#------------------------------------------------------------------------------
# CIE 13.3-1995 color rendering index:
_CIE133_1995 = {'14': getdata(_R_PATH + 'CIE_13_3_1995_R14.dat',kind='np').T}
_CIE133_1995['8'] = _CIE133_1995['14'][0:9].copy()
   
 
#------------------------------------------------------------------------------  
# IES TM30-15 color fidelity and color gamut indices:
_IESTM3015['R'] = {'4880' : {'5nm': getdata(_R_PATH + 'IESTM30_15_R4880.dat',kind='np').T}}
_IESTM3015['R']['99'] = {'1nm' : getdata(_R_PATH + 'IESTM30_15_R99_1nm.dat',kind='np').T}
_IESTM3015['R']['99']['5nm'] = getdata(_R_PATH + 'IESTM30_15_R99_5nm.dat',kind='np').T
temp = getdata(_R_PATH + 'IESTM30_15_R99info.dat',kind='df').values[0]
ies99categories = ['nature','skin','textiles','paints','plastic','printed','color system']
_IESTM3015['R']['99']['info'] = [ies99categories[int(i-1)] for i in temp]


#------------------------------------------------------------------------------
# cie 224:2017 (color fidelity index based on IES TM-30-15):
_CIE224_2017 = {'99': {'1nm' : getdata(_R_PATH + 'CIE224_2017_R99_1nm.dat',kind='np').T}}
_CIE224_2017['99']['5nm'] = getdata(_R_PATH + 'CIE224_2017_R99_5nm.dat',kind='np').T
_CIE224_2017['99']['info'] = _IESTM3015['R']['99']['info']

#------------------------------------------------------------------------------  
# IES TM30-18 color fidelity and color gamut indices:
_IESTM3018['R'] = copy.deepcopy(_IESTM3015['R'])
_IESTM3018['R']['99']['1nm'] = _CIE224_2017['99']['1nm']
_IESTM3018['R']['99']['5nm'] = _CIE224_2017['99']['5nm']


#------------------------------------------------------------------------------
# CRI2012 spectrally uniform mathematical sampleset:
_CRI2012 = {'HL17' : getdata(_R_PATH + 'CRI2012_HL17.dat',kind='np').T}
_CRI2012['HL1000'] = getdata(_R_PATH +'CRI2012_Hybrid14_1000.dat',kind='np').T
_CRI2012['Real210'] = getdata(_R_PATH +'CRI2012_R210.dat',kind='np').T

#------------------------------------------------------------------------------
# MCRI (memory color rendition index, Rm) sampleset:
_MCRI= {'R' : getdata(_R_PATH + 'MCRI_R10.dat',kind='np').T}
_MCRI['info'] = ['apple','banana','orange','lavender','smurf','strawberry yoghurt','sliced cucumber', 'cauliflower','caucasian skin','N4'] # familiar objects, N4: neutral (approx. N4) gray sphere 


#------------------------------------------------------------------------------
# CQS versions 7.5 and 9.0:
_CQS = {'v7.5': getdata(_R_PATH + 'CQSv7dot5.dat',kind='np').T}
_CQS['v9.0'] =  getdata(_R_PATH + 'CQSv9dot0.dat',kind='np').T

#------------------------------------------------------------------------------
# 215 samples proposed by Opstelten, J.J. , 1983, The establishment of a representative set of test colours
# for the specification of the colour rendering properties of light sources, CIE-20th session, Amsterdam. 
_OPSTELTEN215 = {'R' : getdata(_R_PATH + 'Opstelten1983_215.dat',kind='np').T}

#------------------------------------------------------------------------------
# collect in one dict:
_CRI_RFL = {'cie-13.3-1995': _CIE133_1995}
_CRI_RFL['cie-224-2017'] = _CIE224_2017
_CRI_RFL['cri2012'] = _CRI2012
_CRI_RFL['ies-tm30-15'] = _IESTM3015['R']
_CRI_RFL['ies-tm30-18'] = _IESTM3018['R']
_CRI_RFL['ies-tm30'] = _IESTM3018['R']
_CRI_RFL['mcri'] = _MCRI['R']
_CRI_RFL['cqs'] = _CQS

#------------------------------------------------------------------------------
# 1269 Munsell spectral reflectance functions:
_MUNSELL = {'cieobs':'1931_2', 'Lw' : 400.0, 'Yb': 0.2}
_MUNSELL['R'] = getdata(_R_PATH + 'Munsell1269.dat',kind='np').T
temp = getdata(_R_PATH + 'Munsell1269NotationInfo.dat',kind='np',header = 'infer',verbosity=0)
_MUNSELL['H'] = temp[:,1,None]
_MUNSELL['V'] = temp[:,2,None]
_MUNSELL['C'] = temp[:,3,None]
_MUNSELL['h'] = temp[:,4,None]
_MUNSELL['ab'] = temp[:,5:7]

del temp, ies99categories

#------------------------------------------------------------------------------
# 24 MacBeth ColorChecker RFLs
_MACBETH_RFL = {'CC': {'R': getdata(_R_PATH + 'MacbethColorChecker.dat',kind='np').T}}

#------------------------------------------------------------------------------
# 114120 RFLs from https://capbone.com/spectral-reflectance-database/
try:
    _CAPBONE_100K_RFL = {'R': np.load(_R_PATH + 'capbone_100k_rfls.npz')['_CAPBONE_100K_RFL']}
    _CAPBONE_100K_RFL['file'] = _R_PATH + 'capbone_100k_rfls.npz'
except:
    _CAPBONE_100K_RFL = {'R': None}
    _CAPBONE_100K_RFL['file']  = _R_PATH + 'capbone_100k_rfls.npz'
finally:
    _CAPBONE_RFL = {'100k': _CAPBONE_100K_RFL}
    
# Combine RFLs:
_RFL = {'munsell': _MUNSELL, 
         'macbeth':_MACBETH_RFL,
         'capbone': _CAPBONE_RFL,
         'opstelten': _OPSTELTEN215,
         'cri' : _CRI_RFL}
#_RFL.update(_CRI_RFL)