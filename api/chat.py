from fastapi import APIRouter

from schemas.chat import ChatRequest

from services.booking_service import (
    extract_booking_info
)

from services.booking_db_service import (
    save_booking
)

from services.retrieval_service import (
    retrieve_context
)

from services.memory_service import (
    get_history,
    save_history
)

from services.llm_service import (
    generate_response
)

router = APIRouter()


@router.post("/chat")
def chat(
    request: ChatRequest
):

    booking_data = extract_booking_info(
        request.question
    )

    if (
        booking_data
        and booking_data.get("name")
        and booking_data.get("email")
    ):

        save_booking(booking_data)

        return {
            "message": "Interview booked successfully",
            "booking": booking_data
        }

    chunks = retrieve_context(
        request.question
    )

    context = "\n".join(chunks)

    history = get_history(
        request.session_id
    )

    answer = generate_response(
        context=context,
        history=history,
        question=request.question
    )

    save_history(
        request.session_id,
        request.question,
        answer
    )

    return {
        "answer": answer
    }