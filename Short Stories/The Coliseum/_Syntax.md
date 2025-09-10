.angry syntaxing rules

#####----- Tagging ----- #####
## -- Data Tags -- ##
[MD] = Meta_Data
	# Sub-Tag #
	>{IS}_: = Initial_Start
		|HH:MM_A/P_MM:DD:YYYY|
	>{IE}_: = Initial_End
		|HH:MM_A/P_MM:DD:YYYY|
	>{VD}_: = Version_Description
		|Text|

[SD] = Story_Data
	# Sub-Tag #
	>{SD}_: = Story_Description
		|Text|
	>{VB}_: = Overall Vibe
		|Text|
	>{PS}_: = Perspective
		|1| or |2| or |3|
	>{ST}_: = Settings
		|Text|

[WD] = Writers_Data
	# Sub-Tag #
	>{A}_: = Author(s)
		|(Name, Initials)(Name, Initials)|
		? All People who wrote sections of the story
	>{E}_: = Editor(s)
		|(Name, Initials)(Name, Initials)|
		? All people who edited the story or its sections
	>{C}_: = Commentor(s)
		|(Name, Initials)(Name, Initials)|
		? All People who made suggestions
	>{S}_: = Suggestor(s)
		|(Service, Initials)(Service, Initials)|
		? All Service that made suggestions
		
# Data Tag Expectations #
* Start of FILE expects to see *
	> |[Data_Tag]| (expects indented line break)
		>> |{Sub-Tag}_(expects:):_(expects{}){txt}|

## -- Content Tags -- ##
[B]_(txt)_: = Book
	#  Sub-Tags #
	[T]_(txt)_: = Title

	[C#]_(txt)_: = Chapter and Name
		|{C#}_:(expects line break) (expects indent){txt}|
		? Contains Paragraphs and Subsections of the book
	[P#]_(txt)_: = Paragraph_# and Name
		|{P#}_(txt) :(expects line break) (expects indent){txt}|
		? Contains Sub sections of the book
	[SS#]_(txt)_: = SubSection_# and Name
		|{SS#}_(expects line break) (expect indent){txt}|

# Content Tab Expectations #
|[B]| (expects to find this tag)(expect line break)
	
|[Sub-Tag]_(expects (txt))(txt)_(expects:):| (expects indented line break)
	> (expects Sub-Tag)
	
	
## -- Updating Tags -- ##
[U] = Updating/Version Forward Suggestions