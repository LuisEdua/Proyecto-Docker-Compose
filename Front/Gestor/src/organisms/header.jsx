import "bootstrap/dist/css/bootstrap-grid.min.css"
import Title from "../atoms/Title.jsx"
import "../assets/css/header.css"
import Navigator from "../molecules/Navigator.jsx";

function Header() {
    return (
        <header className="bg-primary text-white header d-flex align-items-center">
            <div className="container">
                <div className="row">
                    <div className="col-12 flex-column" id="div-header">
                        <Title>Gestor de Tareas</Title>
                    </div>
                    <div className="col-12 flex-column p-2" >
                        <Navigator></Navigator>
                    </div>
                </div>
            </div>
        </header>
    );
}


export default Header;