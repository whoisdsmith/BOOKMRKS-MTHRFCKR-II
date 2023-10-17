'use strict';

var obsidian = require('obsidian');

const defSnippetFolder = "css-snippets";
class CssSnippetsPlugin extends obsidian.Plugin {
    constructor(app, pluginManifest) {
        super(app, pluginManifest);
    }
    async onload() {
        this.addCommand({
            id: "refresh-styles",
            name: "Reload",
            callback: async () => {
                this.loadSnippets();
            },
        });
        this.addCommand({
            id: "unload-styles",
            name: "Unload",
            callback: async () => {
                this.unloadSnippets();
            },
        });
        this.loadedStyles = Array(0);
        this.loadSnippets();
    }
    onunload() {
        this.unloadSnippets();
    }
    async loadSnippets() {
        this.unloadSnippets();
        // enumerate the style files
        let style_files = await this.app.vault.adapter.list(defSnippetFolder);
        style_files.files;
        for (let fstyle of style_files.files) {
            // console.log( "Found file: ", fstyle );
            if (fstyle.indexOf(".css") < 0) ;
            let content = await this.app.vault.adapter.read(fstyle);
            let css = content;
            var style = document.createElement("style");
            style.innerHTML = css;
            document.head.appendChild(style);
            this.loadedStyles.push(style);
        }
    }
    async unloadSnippets() {
        for (let tag of this.loadedStyles) {
            // console.log( "Removing style tag: ", tag );
            document.head.removeChild(tag);
        }
        this.loadedStyles = Array(0);
    }
}

module.exports = CssSnippetsPlugin;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoibWFpbi5qcyIsInNvdXJjZXMiOlsiLi4vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbbnVsbF0sIm5hbWVzIjpbIlBsdWdpbiJdLCJtYXBwaW5ncyI6Ijs7OztBQUVBLE1BQU0sZ0JBQWdCLEdBQVcsY0FBYyxDQUFDO01BRTNCLGlCQUFrQixTQUFRQSxlQUFNO0lBR25ELFlBQVksR0FBUSxFQUFFLGNBQThCO1FBQ2xELEtBQUssQ0FBQyxHQUFHLEVBQUUsY0FBYyxDQUFDLENBQUM7S0FDNUI7SUFFRCxNQUFNLE1BQU07UUFDVixJQUFJLENBQUMsVUFBVSxDQUFDO1lBQ2QsRUFBRSxFQUFFLGdCQUFnQjtZQUNwQixJQUFJLEVBQUUsUUFBUTtZQUNkLFFBQVEsRUFBRTtnQkFDUixJQUFJLENBQUMsWUFBWSxFQUFFLENBQUM7YUFDckI7U0FDRixDQUFDLENBQUM7UUFFSCxJQUFJLENBQUMsVUFBVSxDQUFDO1lBQ2QsRUFBRSxFQUFFLGVBQWU7WUFDbkIsSUFBSSxFQUFFLFFBQVE7WUFDZCxRQUFRLEVBQUU7Z0JBQ1IsSUFBSSxDQUFDLGNBQWMsRUFBRSxDQUFDO2FBQ3ZCO1NBQ0YsQ0FBQyxDQUFDO1FBRUgsSUFBSSxDQUFDLFlBQVksR0FBRyxLQUFLLENBQW1CLENBQUMsQ0FBQyxDQUFDO1FBQy9DLElBQUksQ0FBQyxZQUFZLEVBQUUsQ0FBQztLQUNyQjtJQUVELFFBQVE7UUFDTixJQUFJLENBQUMsY0FBYyxFQUFFLENBQUM7S0FDdkI7SUFFRCxNQUFNLFlBQVk7UUFDaEIsSUFBSSxDQUFDLGNBQWMsRUFBRSxDQUFDOztRQUd0QixJQUFJLFdBQVcsR0FBRyxNQUFNLElBQUksQ0FBQyxHQUFHLENBQUMsS0FBSyxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUMsZ0JBQWdCLENBQUMsQ0FBQztRQUN0RSxXQUFXLENBQUMsS0FBSyxDQUFDO1FBQ2xCLEtBQUssSUFBSSxNQUFNLElBQUksV0FBVyxDQUFDLEtBQUssRUFBRTs7WUFFcEMsSUFBSSxNQUFNLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxHQUFHLENBQUMsRUFBRSxDQUUvQjtZQUVELElBQUksT0FBTyxHQUFHLE1BQU0sSUFBSSxDQUFDLEdBQUcsQ0FBQyxLQUFLLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsQ0FBQztZQUN4RCxJQUFJLEdBQUcsR0FBRyxPQUFPLENBQUM7WUFFbEIsSUFBSSxLQUFLLEdBQUcsUUFBUSxDQUFDLGFBQWEsQ0FBQyxPQUFPLENBQUMsQ0FBQztZQUM1QyxLQUFLLENBQUMsU0FBUyxHQUFHLEdBQUcsQ0FBQztZQUN0QixRQUFRLENBQUMsSUFBSSxDQUFDLFdBQVcsQ0FBQyxLQUFLLENBQUMsQ0FBQztZQUNqQyxJQUFJLENBQUMsWUFBWSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQztTQUMvQjtLQUNGO0lBRUQsTUFBTSxjQUFjO1FBQ2xCLEtBQUssSUFBSSxHQUFHLElBQUksSUFBSSxDQUFDLFlBQVksRUFBRTs7WUFFakMsUUFBUSxDQUFDLElBQUksQ0FBQyxXQUFXLENBQUMsR0FBRyxDQUFDLENBQUM7U0FDaEM7UUFDRCxJQUFJLENBQUMsWUFBWSxHQUFHLEtBQUssQ0FBbUIsQ0FBQyxDQUFDLENBQUM7S0FDaEQ7Ozs7OyJ9
