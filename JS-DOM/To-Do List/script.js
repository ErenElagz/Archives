/* Variables */
const InputText = document.getElementById('InputText');
const InputButton = document.getElementById('InputButton');
const ListTable = document.getElementById('ListTable');
const UpdateButton = document.getElementsByClassName('UpdateButton');
const DeleteButton = document.getElementsByClassName('DeleteButton');
const DoneButton = document.getElementsByClassName('DoneButton');
let notes = [];

/* Functions */
function DisplayNotes() {
	ListTable.innerHTML = '';
	for (const i of notes) {
		ListTable.insertAdjacentHTML(
			'afterbegin',
			`
                <li class="list-group-item d-flex align-items-center justify-content-between">
                    <p>${i}</p>
                    <div class="d-flex gap-2">
                        <button class="btn btn-primary" onclick="UpdateNote(this)" >
                            <i class="bi bi-pen-fill UpdateButton"></i>
                        </button>
                        <button class="btn btn-success" onclick="CompleteNote(this)" >
                            <i class="bi bi-check2 DoneButton"></i>
                        </button>
                        <button class="btn btn-danger" onclick="DeleteNote(this)" >
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
	console.log(x);
}

/* Update Note */
function UpdateNote(x) {
	console.log(x);
}

/* Complete Note */
function CompleteNote(x) {
	console.log(x);
}
