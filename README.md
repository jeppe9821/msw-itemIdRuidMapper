# msw-itemIdRuidMapper
This tool maps a table of Maplestory item data to a representative data table for Maplestory Worlds (MSW). It automatically groups items depending on type into different tables which can be imported as a csv file

## Example Input
	02000000		Red Potion	A potion made out of red herbs.\nRecovers 50 HP.	info.price=25,  spec.hp=50  

## Example Output
Id	Name	IconRUID	Description	Metadata
2000000	Red Potion	873b727f30ea41efb179d6537009413e	A potion made out of red herbs.\nRecovers 50 HP.	info.price=25,  spec.hp=50  