#TYPEN TODO

This TODO list gives a brief summary of features added on the TypePen Desktop App.
Before you proceed, take at a look of some terms and what the mean

1. `Status`
   The status block indicates if a feature is Recommended or not. Currently they are just Three types of status flags namely:

   - `Recommended`
     Feature has been marked as one to be added to the application
   - `Optional`
     Feature has been determined not to be a requirement for the application but can be included.
   - `Unknown`
     Feature is not necessarily a bad one, but maybe to large(based on the number of contributors) or it's just not worth it but it's doable. This unknown flag will be used if the feature is no where to be found amongst the other two categories

2. `Status codes`
   The status codes are simply numbers indicating if the feature added is working well or needs some improvement.
   _Note_: The codes used here are not in anyway related to a standard convention

   - `200`
     Feature is running smoothly and is stable
   - `302`
     Feature is running but requires improvements in one/or/all the following [functionality, code quality, scalability, readability, dependencies, user experience]
   - `404`
     Feature is no longer working or encountered a bug

### NOTE: This document might be updated or changed at anytime per the circumstances

## Current Features Added

- [x] Create Notes(.typen files) -> 200
- [x] Save Notes(.typen files) -> 302
- [x] Edit Notes(.typen files) -> 302
- [x] Open Notes(.typen files) -> 200
  - [x] Open notes _Only from the default storage location of .typen files_ -> 200
- [x] Text Manipulation -> 200
  - [x] bold
  - [x] Italics
  - [x] Underline
- [x] Recent files Tab -> 302
  - [x] Files saved in a default directory
- [x] Delete note files (.typen extension) -> 200

## Features not added (Very essenstial for a typical notepad)

- [ ] Persistent Storage <br>
      `TypePen should be able to save Files been opened using the open feature. User should not be prompted with a dialog to save a file with another file name when it was opened using the open function`
  - Status: `Recommended`
- [ ] Improved Text Manipulation <br>
      `Currently, Only three text Manipulation techniques are available namely bold, italics and underline. TypePen should support Heading, fonts, fontsize`

  - Status: `Recommended`

- [ ] Support for markdown <br>
      `A typical windows notepad doesn't support markdown. TypePen should have it's own markdown editor including a live previewer.`

  - Status: `optional`

- [ ] Support other file formats <br>
      `TypePen by default supports .typen files only. Extending the functionality to accept multiple file formats with various encoding formats `

  - Status: `Recommended | optional`

- [ ] Autosave <br>
      `TypePen currently supports only manual saving of files. An autosave feature will increase user interaction`

  - Status: `Recommended`

- [ ] Settings Tab <br>
      `Users should be allowed to make some changes to their editor like enable dark mode, toggle autosave on/off, markdown mode(if available) etc. A settings tab should be provided. The settings tab can be updated and changes reflected once changed. Persistent setting management.`

  - Status: `Recommended`

- [ ] Complete RTF Editor <br>
      `For now, TypePen is just a minified RTF editor. We should be able to support basic RTF editing and rendering for rtf files and save them with .rtf extension`

  - Status: `Optional`

- [ ] Font package <br>
      `Users can import their own fonts and load them. And this will be visible for them to toggle their recently added form.`

  - Status: `Recommended`

- [ ] Plugins support <br>
      `TypePen could have access to plugins which can help TypePen be a modularized application. Rather than stack everything, we can turn those features to plugins to enrich the editor.`
  - Status: `Unknown`

### Disclaimer:

This project is not the next Microsoft VS Code. It's a nice project to play around and see what it can turn out to be. Who knows, we might actually make something out of it
