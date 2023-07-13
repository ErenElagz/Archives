/* Variables */
const InputText = document.getElementById('InputText');
const InputButton = document.getElementById('InputButton');
const ListTable = document.getElementById('ListTable');
const UpdateButton = document.getElementsByClassName('UpdateButton');
const DeleteButton = document.getElementsByClassName('DeleteButton');
let notes = [];

/* Functions */
function DisplayNotes() {
	ListTable.innerHTML = '';
	for (const i of notes) {
		ListTable.insertAdjacentHTML(
			'afterbegin',
			`
                <li class="list-group-item d-flex align-items-center justify-content-between">
                    <div>
                        ${i}
                    </div>
                    <div class="d-flex gap-2">
                        <button class="btn btn-primary">
                            <i class="bi bi-pen-fill UpdateButton" ></i>
                        </button>
                        <button class="btn btn-danger">
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
function DeleteNote() {

}

/* Update Note */
function UpdateNote() {

}
