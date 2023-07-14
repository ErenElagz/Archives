/* Variables */
const InputText = document.getElementById('InputText');
const InputButton = document.getElementById('InputButton');
const ListTable = document.getElementById('ListTable');
const UpdateButton = document.getElementsByClassName('UpdateButton');
const DeleteButton = document.getElementsByClassName('DeleteButton');
const DoneButton = document.getElementsByClassName('DoneButton');
let notes = ['Elma Al', 'Armut Al'];

/* Functions */
function DisplayNotes() {
	ListTable.innerHTML = '';
	for (const i of notes) {
		ListTable.insertAdjacentHTML(
			'beforeend',
			`<li class="list-group-item d-flex align-items-center justify-content-between">
				<p class="m-0">${i}</p>
				<div class="d-flex gap-2">
					<button class="btn btn-primary" onclick="UpdateNote(this)" value="${notes.indexOf(
						i
					)}">
						<i class="bi bi-pen-fill UpdateButton"></i>
					</button>
					<button class="btn btn-success" onclick="CompleteNote(this)" value="${notes.indexOf(
						i
					)}">
						<i class="bi bi-check2 DoneButton"></i>
					</button>
					<button class="btn btn-danger" onclick="DeleteNote(this)" value="${notes.indexOf(
						i
					)}">
						<i class="bi bi-trash-fill DeleteButton" ></i>
					</button>
				</div>
			</li>`
		);
	}
}

/* Add Note */
function AddNote() {
	if (InputText.value == '') {
		alert('Note Cant be Empty!');
	} else {
		notes.push(InputText.value);
		InputText.value = '';
		DisplayNotes();
	}
}

/* Delete Note */
function DeleteNote(x) {
	notes.splice(x.value,1);
	DisplayNotes();
}

/* Update Note */
function UpdateNote(x) {
	InputText.value = notes[x.value]
	if (InputText.value == '') {
		alert('Note Cant be Empty!');
	} else {
		notes[x.value] = InputText.value
		DisplayNotes()
	}
}

/* Complete Note */
function CompleteNote(x) {
	console.log(x.value);
}
