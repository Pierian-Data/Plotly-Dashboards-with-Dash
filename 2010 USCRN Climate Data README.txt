                          USCRN/USRCRN HOURLY FILES

                            UPDATED: 2017-07-06 
                              
README CONTENTS:                          
    1. GENERAL INFORMATION 
    2. DATA VERSION / STATUS UPDATES
    3. DIRECTORY ORGANIZATION
    4. FILE AND FILENAME FORMATS
        A. YEARLY
        B. SNAPSHOTS
        C. UPDATES
    5. DATA FIELDS / FORMATS / IMPORTANT NOTES

********************************************************************************

1. GENERAL INFORMATION

NCDC provides access to hourly data from the U.S. Climate Reference Network / 
U.S. Regional Climate Reference Network (USCRN/USRCRN) via anonymous ftp at:

        ftp://ftp.ncdc.noaa.gov/pub/data/uscrn/products/hourly02
        
and an identical web interface at:

        http://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02
        
Before using these data, be sure to review this document carefully, as well
as any announcements within the main (hourly02) directory. 

********************************************************************************

2. DATA VERSION / STATUS UPDATES

Status and Version Information for U.S. Climate Reference Network Data

  ##########################
  
Version change:     2.1 to 2.1.1
Commencement Date:  2017-06-20
Completion Date:    2017-06-30
Variables impacted: Precipitation

    Effective June 30, 2017, recalculation using the Official Algorithm
for Precipitation (OAP) 2.1.1 has been completed. The purpose of this 
recalculation is described in Appendix A of the OAP 2.1 documentation:
https://www1.ncdc.noaa.gov/pub/data/uscrn/documentation/maintenance/2016-05/USCRN_OAP2.1.Description_PrecipChanges.pdf

  ##########################
  
Status change:      Correction
Correction Applied: 2017-05-01
Variables impacted: Precipitation for 3 stations
	
    From July 2016 until May 1, 2017, the precipitation values for 
the following stations and time periods were mistakenly missing on 
the website and in the FTP product files:
		NC Asheville 8 SSW          2004-05-01 to 2004-11-01 
		SC McClellanville 7 NE      2005-05-01 to 2005-11-01
		CA Stovepipe Wells 1 SW     2004-05-01 to 2005-06-01
Precipitation data for these stations/time periods that were downloaded
during the affected time period should be re-acquired. 

  ##########################
  
Version change:     2.0 to 2.1 
Commencement Date:  2016-05-12 
Completion Date:    2016-06-13
Variables impacted: Precipitation
                    Relative Humidity (RH)
                    Temperatures from RH Sensor
                    Thermometer Shield Aspiration Fan Speeds
                    Air Temperature (when fan speeds are low)
                      
    Beginning May 12, 2016, USCRN changed the current data set to 
version 2.1 from v2.0. This version change was retroactively applied to 
all USCRN/USRCRN stations for their period-of-record 5-minute measurements 
from 2016-05-12 until 2016-06-13. [Note that during this period of 
reprocessing, data on the website and in these FTP products contained 
a mixture of v2.0 and v2.1 values.]
    Version 2.1 includes minor precipitation algorithm changes and 
changes/additions to the quality control ranges for acceptable 
relative humidity (RH) values, temperatures measured with the 
RH sensors, and for the speed of the fans which are used to 
aspirate the air temperature sensors. For precipitation, the Official 
Algorithm for Precipitation (OAP) v2.1 was implemented which  
addresses a minor correction to v2.0 that guards against
overally large (> 0.3 mm) precipitation residuals from one hour 
being transferred to the next hour. Further information can be found at 
http://www.ncdc.noaa.gov/crn/documentation.html.

  ##########################
  
Version change:     1.0 to 2.0 
Commencement Date:  2015-08-17
Completion Date:    2015-09-15
Variables impacted: Precipitation

    The original Official Algorithm for Precipitation 
(OAP) version 1.0 was operational until August 17, 2015 and used a 
pairwise comparison and moving reference depth to calculate 
precipitation. Precipitation data accessed and/or downloaded 
prior to this date were calculated using OAP v1.0. 
    Beginning August 17, 2015, all precipitation data were 
calculated using a new processing algorithm, OAP v2.0. In addition, 
the v2.0 algorithm was retroactively applied to all USCRN/USRCRN 
stations for their periods of record (PORs) starting when 5-minute 
data began being collected. The reprocessing took approximately four
weeks to recalculate all station's existing values from v1.0 to v2.0
for their PORs and was completed on September 15, 2015. 
    OAP v2.0 marked a fundamental shift in the procedures used to calculate 
precipitation. The new algorithm uses a weighted average approach 
based on each sensor's noise level. It has greatly improved the 
network's capacity to detect lighter precipitation with greater 
confidence. For details, see Leeper et. al., 2015, 
(http://journals.ametsoc.org/doi/abs/10.1175/JTECH-D-14-00185.1) and
http://www.ncdc.noaa.gov/crn/documentation.html.

********************************************************************************

3. DIRECTORY ORGANIZATION

The hourly02 directory contains the following subdirectories:

    - /2000 through the present year 
        -- useful for obtaining the most up-to-date data from one or more 
        stations for a particular year or years (typically updated on an hourly 
        basis).
    
    - /snapshots 
        -- useful for obtaining data from all stations for all years. 
        The entire dataset (as of the date/time of the filename) can be 
        downloaded in a single compressed file. New snapshot files are created 
        on a regular basis; the most recent file contains the most recent set 
        of data.
    
    - /updates 
        -- real-time files broadcast over NOAAPort; stored in yearly 
        subdirectories. These files contain hourly values for all stations. 
    
********************************************************************************
        
4. FILE AND FILENAME FORMATS

  A. YEARLY

    Each yearly subdirectory in hourly02 contains one file for each USCRN/USRCRN 
    station listing its hourly data in ASCII text format. The files are named 
    according to the following convention:

                CRNH02TT-YYYY-${name}.txt

       CRNH02 = filename prefix to denote CRN hourly02 data 
           TT = 2-character file format number (currently 03)
         YYYY = 4-digit year
      ${name} = station name (state location vector) (e.g. AZ_Tucson_11_W)

    The 2-character sequence TT indicates the file format number and is updated 
    when the file format is changed. Previous changes were applied retroactively
    for all years and are outlined below:

     1. [Transition from format '01' to '02']
        On March 22, 2011 15:00 UTC the format of the hourly product was
        changed by removing the COOPNO (Cooperative Observer Program Number)
        column. This had been the second column in the format, starting at 
        character 7 and ending at character 12. With the removal of 
        this column, all following columns were shifted to the left by
        7 characters. The contents of the shifted columns remained the same.

     2. [Transition from format '02' to '03']
        On January 7, 2013 15:00 UTC the format of the hourly product was
        changed by adding the SUR_TEMP_TYPE column. This became the 
        20th column in the format, starting and ending at character 125. 
        With the addition of this column, all the following columns were 
        shifted to the right by 2 characters. The contents of the shifted 
        columns remained the same.
                
  B. SNAPSHOTS

    The 'snapshots' directory contains a series of compressed (.zip) files. 
    Each file contains the entire data archive of USCRN/USRCRN hourly02 data as 
    of the date/time shown on its filename. Once uncompressed, the directory and
    file structure are identical to the yearly subdirectories (as explained 
    above). Snapshots are created and uploaded at regular intervals, and are 
    named according to the following convention:

                CRNH02TT-YYYYMMDDHHmm.zip
    
       CRNH02 = filename prefix to denote CRN hourly02 data
           TT = 2-character file format number (see above)
         YYYY = 4-digit year files generated
           MM = 2-digit month files generated (01=Jan, ..., 12=Dec)
           DD = 2-digit day of month files generated
           HH = 2-digit hour of day files generated
           mm = 2-digit minute files generated

    Users may obtain the most recent archive of data for all stations and all 
    years by downloading the most recent file in this directory. As improvements
    to the dataset are made, the snapshot files serve as a historical record of 
    the archive through time.
    
  C. UPDATES
                
    The 'updates' directory contains a record of the real-time files which are 
    produced hourly and broadcast over NOAAPort (SXXX91 CRNH02). The 
    yearly subdirectories contain a collection of ASCII files named according 
    to the following convention:

                CRNFFH02TT-YYYYMMDDHHmm.txt

           FF = 2-digit file frequency, in minutes (60)
          H02 = filename prefix to denote CRN hourly02 data
           TT = 2-character file format number (see above)
         YYYY = 4-digit year
           MM = 2-digit month (01=Jan, ..., 12=Dec)
           DD = 2-digit day of month
           HH = 2-digit hour of day
           mm = 2-digit minute
           
    Each file contains all the USCRN/USRCRN hourly data from every station 
    loaded into the database since the last transmission (during the period of 
    time lasting 'FF' minutes and ending at the UTC time YYYYMMDDHHmm). Note 
    that 'updates' files are *not* named according to the observation time. 
    Data from stations generally arrives at NCDC and are loaded into the 
    database steadily throughout the hour, however sometimes an observation is 
    relayed several hours later (due to temporary transmission problems, etc). 
    
********************************************************************************

5. DATA FIELDS / FORMATS

Each station file contains fixed-width formatted fields with a single hour's 
data per line. A summary table of the fields and a detailed listing of field 
definitions/column formats are shown below. 

Fortran users will find the column widths and counts useful. 

The file "HEADERS.txt", found in the hourly02 directory, is designed to be 
prepended to the data for use with spreadsheet programs, data extraction tools 
(e.g. awk) or any other programming language. This file contains the following 
three lines:

    1. Field Number
    2. Field Name
    3. Unit of Measure

Please be sure to refer to the "Important Notes" section below for essential 
information.

All hourly data are calculated over the 60-minute period *ending* at the UTC 
and LST times shown. Please note that the station's Local Standard Time is 
always used, regardless of its Daylight Savings status. 

Field#  Name                           Units
---------------------------------------------
   1    WBANNO                         XXXXX
   2    UTC_DATE                       YYYYMMDD
   3    UTC_TIME                       HHmm
   4    LST_DATE                       YYYYMMDD
   5    LST_TIME                       HHmm
   6    CRX_VN                         XXXXXX
   7    LONGITUDE                      Decimal_degrees
   8    LATITUDE                       Decimal_degrees
   9    T_CALC                         Celsius
   10   T_HR_AVG                       Celsius
   11   T_MAX                          Celsius
   12   T_MIN                          Celsius
   13   P_CALC                         mm
   14   SOLARAD                        W/m^2
   15   SOLARAD_FLAG                   X
   16   SOLARAD_MAX                    W/m^2
   17   SOLARAD_MAX_FLAG               X
   18   SOLARAD_MIN                    W/m^2
   19   SOLARAD_MIN_FLAG               X
   20   SUR_TEMP_TYPE                  X
   21   SUR_TEMP                       Celsius
   22   SUR_TEMP_FLAG                  X
   23   SUR_TEMP_MAX                   Celsius
   24   SUR_TEMP_MAX_FLAG              X
   25   SUR_TEMP_MIN                   Celsius
   26   SUR_TEMP_MIN_FLAG              X
   27   RH_HR_AVG                      %
   28   RH_HR_AVG_FLAG                 X
   29   SOIL_MOISTURE_5                m^3/m^3
   30   SOIL_MOISTURE_10               m^3/m^3
   31   SOIL_MOISTURE_20               m^3/m^3
   32   SOIL_MOISTURE_50               m^3/m^3
   33   SOIL_MOISTURE_100              m^3/m^3
   34   SOIL_TEMP_5                    Celsius
   35   SOIL_TEMP_10                   Celsius
   36   SOIL_TEMP_20                   Celsius
   37   SOIL_TEMP_50                   Celsius
   38   SOIL_TEMP_100                  Celsius

   1    WBANNO  [5 chars]  cols 1 -- 5 
          The station WBAN number.

   2    UTC_DATE  [8 chars]  cols 7 -- 14 
          The UTC date of the observation.

   3    UTC_TIME  [4 chars]  cols 16 -- 19 
          The UTC time of the observation. Time is the end of the observed 
          hour, so the 0000 hour is actually the last hour of the previous 
          day's observation (starting just after 11:00 PM through midnight).

   4    LST_DATE  [8 chars]  cols 21 -- 28 
          The Local Standard Time (LST) date of the observation.

   5    LST_TIME  [4 chars]  cols 30 -- 33 
          The Local Standard Time (LST) time of the observation. Time is the 
          end of the observed hour (see UTC_TIME description).

   6    CRX_VN  [6 chars]  cols 35 -- 40 
          The version number of the station datalogger program that was in 
          effect at the time of the observation. Note: This field should be 
          treated as text (i.e. string).

   7    LONGITUDE  [7 chars]  cols 42 -- 48 
          Station longitude, using WGS-84.

   8    LATITUDE  [7 chars]  cols 50 -- 56 
          Station latitude, using WGS-84.

   9    T_CALC  [7 chars]  cols 58 -- 64 
          Average air temperature, in degrees C, during the last 5 minutes 
          of the hour. See Note F.

   10   T_HR_AVG  [7 chars]  cols 66 -- 72 
          Average air temperature, in degrees C, for the entire hour. See Note 
          F.

   11   T_MAX  [7 chars]  cols 74 -- 80 
          Maximum air temperature, in degrees C, during the hour. See Note 
          F.

   12   T_MIN  [7 chars]  cols 82 -- 88 
          Minimum air temperature, in degrees C, during the hour. See Note 
          F.

   13   P_CALC  [7 chars]  cols 90 -- 96 
          Total amount of precipitation, in mm, recorded during the hour. See 
          Note F.

   14   SOLARAD  [6 chars]  cols 98 -- 103 
          Average global solar radiation, in watts/meter^2.

   15   SOLARAD_FLAG  [1 chars]  cols 105 -- 105 
          QC flag for average global solar radiation. See Note G.

   16   SOLARAD_MAX  [6 chars]  cols 107 -- 112 
          Maximum global solar radiation, in watts/meter^2.

   17   SOLARAD_MAX_FLAG  [1 chars]  cols 114 -- 114 
          QC flag for maximum global solar radiation. See Note G.

   18   SOLARAD_MIN  [6 chars]  cols 116 -- 121 
          Minimum global solar radiation, in watts/meter^2.

   19   SOLARAD_MIN_FLAG  [1 chars]  cols 123 -- 123 
          QC flag for minimum global solar radiation. See Note G.

   20   SUR_TEMP_TYPE  [1 chars]  cols 125 -- 125 
          Type of infrared surface temperature measurement: 'R' denotes raw 
          (uncorrected), 'C' denotes corrected, and 'U' when unknown/missing. 
          See Note H.

   21   SUR_TEMP  [7 chars]  cols 127 -- 133 
          Average infrared surface temperature, in degrees C. See Note H.

   22   SUR_TEMP_FLAG  [1 chars]  cols 135 -- 135 
          QC flag for infrared surface temperature. See Note G.

   23   SUR_TEMP_MAX  [7 chars]  cols 137 -- 143 
          Maximum infrared surface temperature, in degrees C.

   24   SUR_TEMP_MAX_FLAG  [1 chars]  cols 145 -- 145 
          QC flag for infrared surface temperature maximum. See Note G.

   25   SUR_TEMP_MIN  [7 chars]  cols 147 -- 153 
          Minimum infrared surface temperature, in degrees C.

   26   SUR_TEMP_MIN_FLAG  [1 chars]  cols 155 -- 155 
          QC flag for infrared surface temperature minimum. See Note G.

   27   RH_HR_AVG  [5 chars]  cols 157 -- 161 
          RH average for hour, in percentage. See Note I.

   28   RH_HR_AVG_FLAG  [1 chars]  cols 163 -- 163 
          QC flag for RH average. See Note G.

   29   SOIL_MOISTURE_5  [7 chars]  cols 165 -- 171 
          Average soil moisture at 5 cm below the surface, in m^3/m^3. See 
          Note K.

   30   SOIL_MOISTURE_10  [7 chars]  cols 173 -- 179 
          Average soil moisture at 10 cm below the surface, in m^3/m^3. See 
          Note K.

   31   SOIL_MOISTURE_20  [7 chars]  cols 181 -- 187 
          Average soil moisture at 20 cm below the surface, in m^3/m^3. See 
          Note K.

   32   SOIL_MOISTURE_50  [7 chars]  cols 189 -- 195 
          Average soil moisture at 50 cm below the surface, in m^3/m^3. See 
          Note K.

   33   SOIL_MOISTURE_100  [7 chars]  cols 197 -- 203 
          Average soil moisture at 100 cm below the surface, in m^3/m^3. See 
          Note K.

   34   SOIL_TEMP_5  [7 chars]  cols 205 -- 211 
          Average soil temperature at 5 cm below the surface, in degrees C. 
          See Note K.

   35   SOIL_TEMP_10  [7 chars]  cols 213 -- 219 
          Average soil temperature at 10 cm below the surface, in degrees C. 
          See Note K.

   36   SOIL_TEMP_20  [7 chars]  cols 221 -- 227 
          Average soil temperature at 20 cm below the surface, in degrees C. 
          See Note K.

   37   SOIL_TEMP_50  [7 chars]  cols 229 -- 235 
          Average soil temperature at 50 cm below the surface, in degrees C. 
          See Note K.

   38   SOIL_TEMP_100  [7 chars]  cols 237 -- 243 
          Average soil temperature at 100 cm below the surface, in degrees 
          C. See Note K.

    IMPORTANT NOTES:
        A.  All fields are separated from adjacent fields by at least one space.
        B.  Leading zeros are omitted.
        C.  Missing data are indicated by the lowest possible integer for a 
            given column format, such as -9999.0 for 7-character fields with 
            one decimal place or -99.000 for 7-character fields with three
            decimal places.
        D.  Hourly data are calculated over the 60-minute period *ending*
            at the time shown.
        E.  Calculated fields, such as T_CALC and P_CALC, do not have quality 
            flags associated with them because these are derived quantities 
            from raw data. When the raw data used in the calculation are 
            flagged as erroneous, the derived values are not calculated, and 
            are instead reported as missing. Therefore, these fields may be 
            assumed to always be good (unflagged) data, except when they are 
            reported as missing.
        F.  The hourly values reported in this dataset are calculated using 
            multiple independent measurements for temperature and precipitation. 
            USCRN/USRCRN stations have multiple co-located temperature sensors 
            that make 10-second independent measurements which are used to 
            produce max/min/avg temperature values at 5-minute intervals. The
            precipitation gauge is equipped with multiple load cell sensors to 
            provide independent measurements of depth change at 5-minute 
            intervals.  
        G.  Quality control flags indicate the following: 0 denotes good data 
            and 3 denotes erroneous data.
        H.  On 2013-01-07 at 1500 UTC, USCRN began reporting corrected surface 
            temperature measurements for some stations. These changes  
            impact previous users of the data because the corrected values 
            differ from uncorrected values. To distinguish between uncorrected 
            (raw) and corrected surface temperature measurements, a surface 
            temperature type field was added to the data product. The 
            possible values of the this field are "R" to denote raw surface 
            temperature measurements, "C" to denote corrected surface 
            temperature measurements, and "U" for unknown/missing.
        I.  Hourly relative humidity is computed from 5-minute averages in 
            almost all cases, however the two Asheville, NC stations reported 
            only hourly RH values until 2007-02-22.
        J.  USRCRN stations do not measure solar radiation, surface temperature,
            relative humidity or soil variables, so those fields are shown as 
            missing data.
        K.  USCRN stations have multiple co-located soil sensors that record 
            independent measurements at 5-minute intervals. The hourly soil 
            values reported in this dataset are calculated from these multiple 
            independent measurements. Average soil moisture (volumetric water 
            content) is the ratio of water volume over sample volume 
            (m^3 water/m^3 soil).
        L.  In accordance with Service Change Notice 14-25 from the National 
            Weather Service, NCDC stopped providing data from the 72 
            Southwest Regional Climate Reference Network (USRCRN) stations on 
            June 1, 2014. The historical data for these stations remain 
            available. 
        M.  This product supersedes the hourly01 files. It contains all of the
            variables from the earlier product, plus additional ones. 
