function scrambledString(tag, objName, initScrambledString, initScrambledStringIndices) {
	this.tag = tag;
	this.objName = objName;
	this.string = initScrambledString;
	this.indices = initScrambledStringIndices;
	this.rescramble = rescramble;
	this.initAnimatedBubbleSort = initAnimatedBubbleSort;
	this.bubbleSortStep = bubbleSortStep;
	this.bubbleSortBookmark = 0;

	this.rescramble();
	this.tag.innerHTML = '<a href="#" style="word-wrap: break-word">'+this.string+' </a>';
}

function rescramble() {
	for (i = 0; i < this.indices.length; i++) {
		indexToMove = Math.floor(Math.random() * (this.indices.length - i));
		charIndexRemoved = this.indices.splice(indexToMove, 1);
		this.indices = this.indices.concat(charIndexRemoved);
		scrambledStringTemp = this.string.substring(0, indexToMove) +
			this.string.substring(indexToMove + 1) +
			this.string.substring(indexToMove, indexToMove + 1);
		this.string = scrambledStringTemp;
	}
}

function initAnimatedBubbleSort() {
	this.interval = setInterval(this.objName + '.bubbleSortStep()', 1);
}

function bubbleSortStep() {		
	if (this.bubbleSortBookmark >= this.indices.length - 1) {
		this.bubbleSortBookmark = 0;
	}
	for (i = this.bubbleSortBookmark; i < this.indices.length - 1; i++) {
		if (i == 0) {
			this.changed = 0;
		}
		if (this.indices[i] > this.indices[i + 1]) {
			this.changed = 1;
			tempIndex = this.indices[i];
			this.indices[i] = this.indices[i + 1];
			this.indices[i + 1] = tempIndex;
			tempArrange = this.string.substring(0, i) +
				this.string.substring(i + 1, i + 2) + 
				this.string.substring(i, i + 1) +
				this.string.substring(i + 2);
			this.string = tempArrange;
			this.tag.innerHTML = '<a href="mailto:'+ this.string +'" style="word-wrap: break-word">'+this.string+' </a>';
			this.bubbleSortBookmark = i;
			break;
		}
	}
	this.bubbleSortBookmark = i;
	if (!this.changed) {
		clearInterval(this.interval);
	}
}