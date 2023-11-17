import "bootstrap/dist/css/bootstrap-grid.min.css"

export default function Title(props) {
    return (
        <div>
            <h1>{props.children}</h1>
        </div>
    );
}