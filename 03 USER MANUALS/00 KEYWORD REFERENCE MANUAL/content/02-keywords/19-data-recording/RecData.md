# RecData

RecData is an array that holds all the information pertaining the latest recording. This data is best
viewed as a graph using agito's PC Suite. The information below is mainly useful for a user that
wants to write their own software to analyze the data.
Use RecUpload to receive a comma delimited list of the values in RecData. Note that RecUpload
does not only upload the values as they are but also converts them if needed to values that are
useful to the user. Some of the conversions use internal ratios, so the user cannot repeat them.
The values of RecData can be accessed individually by querying RecData[n]. This is not
recommended for the obvious reason that it is inconvenient, but also because RecUpload will
convert the raw data to user data.

                                                                                                      Page 490

            Tel: +972-9-8909797 Fax: +972-9-8909796 email: info@agito.co.il website: www.agito.co.il
